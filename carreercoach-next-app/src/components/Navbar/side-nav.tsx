import { Button } from "@nextui-org/button";
import { Input } from "@nextui-org/input";
import {
  Navbar,
  NavbarBrand,
  NavbarContent,
  NavbarItem,
} from "@nextui-org/navbar";

export default function SideNav() {
  return (
    <nav className="md:w-[350px] bg-slate-200 py-4 px-6 rounded-xl flex flex-col transition-width duration-500 h-[calc(100vh - 0.75rem) justify-start items-center">
      <div className="flex w-full flex-col items-center justify-center">
        <div className="w-full gap-4 flex flex-col">
          <div className="h-10 flex items-center justify-start">
            <p className=" font-bold text-black">URL</p>
          </div>
          <div className="flex flex-col justify-center items-center gap-4">
            <Input placeholder="url" fullWidth />
            <div className="flex items-center justify-center">
              <Button color="primary">Generate Questions</Button>
            </div>
          </div>
          <div className="bg-black mt-6">Generated questions</div>
        </div>
      </div>
    </nav>
  );
}
