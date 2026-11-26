# The original edge kernel on complex angular rectangles

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

Theorem 3 in Section 6 proves the full original kernel expansion on
\(|\Re t|,|\Re u|\le\pi/2\), \(|\Im t|,|\Im u|\le3/10\),
including both level parities and ordinary boundary derivatives.
Section 5 proves the intermediate width-one rectangle; the earlier
thin-rectangle proof is retained as well.

The wider proofs separate the constant and nonconstant parts of the
cotangent contour, retain every original Newton index, and control
all endpoint integrals. The final extension uses a rigorous
fixed-patch endpoint certificate together with analytic bounds for
the other regions. It proves the coefficient of the finite sum;
the classical Hessian alone would not establish that coefficient.

Put
\[
 \mathcal B_0=\{t:|\Re t|\le1,\ |\Im t|\le1/200\},\qquad
 I=[9/50,3/10],\qquad h=1/500,
 \tag{1}
\]
and use the original normalization
\[
 K_N(t,u)=\sum_{k=0}^{N-1}e_k(-2\cos t)e_k(-2\cos u),\qquad
 e_k(z)=S_k^{-2}\prod_{j<k}(2\cos((2j+1)\pi/N)-z).
 \tag{2}
\]
The functions \(J,b,A,\psi\) below have their original branches:
\[
 \begin{split}
 J'(x)&=\Log(2\sin\pi x),\qquad J(0)=0,\\
 b(x,t)&=-J(1/2-x+t/(2\pi))-J(1/2-x-t/(2\pi))-2J(x),\\
 A(x,t,u)&=b(x,t)+b(x,u),\qquad
 \psi(t,u)=A(x_*(t,u),t,u),\quad x_*(0,0)=1/4.
 \end{split}
 \tag{3}
\]
All arguments in (3) have real part strictly between zero and one
on the wire rectangle used below. These are ordinary holomorphic
branches there, including at zero angular height.

**Theorem 1.** On a neighborhood of \(\mathcal B_0^2\), the full
original kernel has the uniform expansion
\[
 K_N(t,u)=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}(1+O(N^{-1})),
 \qquad
 a_e(t,u)=\frac{\sqrt{2\pi}}
 {4\sin^2(\pi x_*)\sqrt{-A_{xx}(x_*,t,u)}}.
 \tag{4}
\]
The amplitude is holomorphic and nonzero. The square root is positive
at \((t,u)=(0,0)\), where \(a_e=1/4\). The normalized error is
holomorphic, has an expansion to every fixed inverse-power order,
and retains all fixed parameter derivatives on a smaller
neighborhood. In particular (4) holds through both level parities
with every ordinary free-boundary normal retained. It implies
eventual nonvanishing uniformly on the displayed compact box.

## 1. The saddle lies inside one uniform wire rectangle

Write \(c=\cos t=a+ib\), \(d=\cos u=a'+ib'\), and
\[
 C=\frac{1-cd}{2+c+d},\qquad
 x_*=(2\pi)^{-1}\arccos C.
 \tag{5}
\]
Throughout (1), elementary Taylor bounds give
\[
 27/50<a,a'<10001/10000=:a_1,\qquad |b|,|b'|<1/190=:b_1.
 \tag{6}
\]
Let \(p=2+a+a'\), \(e=b+b'\), and \(n_0=1-aa'\).
The real comparison \(n_0/p\) lies between \(-1/20000\) and
\(23/100\), since it decreases in each of \(a,a'\). Direct division
in (5) shows
\[
 \left|\Re C-\frac{n_0}{p}\right|
 \le b_1^2\left(\frac13+\frac{4a_1}{9}+\frac4{27}\right)
 <\frac1{30000}.
 \tag{7}
\]
Here \(p>3\) and \(|n_0|<1\) were used; the estimate keeps the
quadratic imaginary correction, rather than an absolute first-order
complex bound. Also the exact imaginary numerator is
\[
 \Im C=-\frac{b|1+d|^2+b'|1+c|^2}{|2+c+d|^2},
 \qquad
 |Im C|\le\frac{2b_1((1+a_1)^2+b_1^2)}9<\frac1{200}.
 \tag{8}
\]
Thus \(-1/1000<\Re C<231/1000\). If
\(2\pi x_*=\theta+i\nu\), the principal inverse cosine has
\(0<\theta<\pi\),
\(\cos\theta=\Re C/\cosh\nu\), and
\(|\sinh\nu|=|\Im C|/\sin\theta\). Consequently
\(\sin\theta>9/10\) and
\[
 \boxed{\quad
 21/100<\Re x_*<251/1000,\qquad |\Im x_*|<1/1000.
 \quad}
 \tag{9}
\]
For the real bounds, use
\(\cos(21\pi/50)>\cos(33/25)>6/25\) and
\(\cos(251\pi/500)=-\sin(\pi/500)<-1/1000\).
For the imaginary bound use \(\operatorname{arsinh}s\le s\)
and \(\pi>3\).

The exponential of \(A_x\) at (5) equals one algebraically.
All the factors remain nonzero in the regular factorial strips,
and the parameter box is connected. Hence the logarithmic equation
is exactly \(A_x(x_*,t,u)=0\), as at the complete point; there is
no unrecorded \(2\pi i\) charge. The derivative calculation of the
[original edge packet](../papers/circle-tree-volume/edge-packet.tex)
therefore identifies this phase with the same calibrated edge phase
\(\psi_t=-\pi^{-1}\operatorname{arsinh}(\tan(t/2)\cos(u/2))\).

## 2. Uniform curvature and the exact cotangent contour

On \(x\in I+i[-h,h]\), differentiation gives
\[
 A_{xx}=-\pi\left[
 \sum_{v=t,u}\{\tan(\pi x+v/2)+\tan(\pi x-v/2)\}
                   +4\cot(\pi x)\right].
 \tag{10}
\]
Every real tangent argument belongs to
\([9\pi/50-1/2,3\pi/10+1/2]\subset(0,\pi/2)\);
its cosine exceeds \(1/8\), and its imaginary part has magnitude
less than \(9/1000\). The real part of \(\pi x\) has sine greater
than \(1/2\). The exact formulas for the real and imaginary parts
of tangent and cotangent now imply
\[
 \boxed{\qquad
 \Re A_{xx}<-20,\qquad |\Im A_{xx}|<8,\qquad |A_{xx}|<128.
 \qquad}
 \tag{11}
\]
Here are explicit estimates sufficient for all three constants.
For each tangent argument \(r+iv\),
\(\Re\tan(r+iv)>(99/100)\tan r\),
\(|\Im\tan(r+iv)|<3/5\), and \(|\tan(r+iv)|<8\).
For \(a+iy=\pi x\), the corresponding bounds are
\(\Re\cot(a+iy)>(99/100)\cot a\),
\(|\Im\cot(a+iy)|<13/500\), and \(|\cot(a+iy)|<2\).
For example the real-part attenuation denominators are
\(1+\sinh^2v/\cos^2r<1+64/10000<100/99\) and
\(1+\sinh^2y/\sin^2a<1+4/10000<100/99\).
Convexity of tangent on \((0,\pi/2)\) gives each paired real
tangent sum at least \(2\tan a\). Thus its total with the cotangents
is at least \((99/100)4(\tan a+\cot a)\ge(99/100)8\).
The imaginary and modulus bounds follow respectively from
\(\pi(4\cdot3/5+4\cdot13/500)<8\) and \(40\pi<128\).

Taylor's formula at the actual saddle gives, for
\(X=\Re(x-x_*)\), \(Y=\Im(x-x_*)\),
\[
 \Re(A(x,t,u)-\psi(t,u))
       \le-10X^2+8|XY|+64Y^2.
 \tag{12}
\]
On each vertical side of the wire rectangle,
\(|X|\ge3/100\), \(|Y|\le3/1000\), so the right side is at most
\(-7704/10^6<-7/1000\). On either horizontal side its maximum
over real \(X\) is at most
\[
 (64+64/40)(3/1000)^2=369/625000<1/1000.
 \tag{13}
\]
This is strictly smaller than the nonconstant-cotangent penalty
\(2\pi h>12/1000\), leaving a gap greater than \(1/100\).

Use the exact canonical factorial interpolation
\[
 B_N(x,t)=\frac{N}
 {G_N(N(1/2-x+t/(2\pi))-1/2)
  G_N(N(1/2-x-t/(2\pi))-1/2)G_N(Nx)^2}.
 \tag{14}
\]
It equals \(e_k(-2\cos t)\) at \(x=k/N\), as an ordinary
polynomial identity in the boundary variable. On the rectangle all
scaled factorial real parts stay in a fixed compact subinterval of
\((0,1)\); the smallest is greater than
\(1/5-1/(2\pi)>1/30\). Therefore the original factorial theorem gives
\[
 B_N(x,t)B_N(x,u)
   =\frac{e^{NA(x,t,u)}}{4N^2\sin^2(\pi x)}(1+O(N^{-1})),
 \tag{15}
\]
uniformly and holomorphically, with every fixed further order.

Enclose exactly the retained integers by the residue kernel
\(\pi N\cot(\pi Nx)\), using vertical half-grid sides at distance
\(O(N^{-1})\) from the ends of \(I\), and heights \(\pm h\).
The strict inequalities above persist on these slightly displaced
sides. On the vertical sides the cotangent has modulus at most one.
On the horizontal sides it is \(\mp i+O(e^{-2\pi Nh})\).
Equations (12)--(13) therefore bound every vertical current and
every nonconstant cotangent mode strictly below the selected rate.

The two constant horizontal terms have total coefficient \(+N\)
times the wire integral. Move each to the horizontal through \(x_*\).
The endpoint connectors retain the bound (12). On this line (11)
gives a unique real maximum at the saddle and a uniform negative
second derivative. The ordinary holomorphic Laplace expansion yields
the coefficient (4); its powers are
\(N\cdot N^{-2}\cdot N^{-1/2}=N^{-3/2}\).
This argument proves the coefficient of the actual retained finite
sum, rather than just the existence of a critical point.

## 3. All omitted original indices

The exact consecutive-product relation is
\[
 e_{k+1}(-2\cos t)=e_k(-2\cos t)
 \frac{2\cos((2k+1)\pi/N)+2\cos t}{4\sin^2((k+1)\pi/N)}.
 \tag{16}
\]
Below \(k/N=9/50+O(N^{-1})\), the multiplier has modulus
uniformly greater than one. Indeed its limiting real numerator is
greater than \(2(2/5+1/2)\), and its denominator is less than
\(4\cdot3/10\), giving a ratio greater than \(3/2\).
Above \(k/N=3/10+O(N^{-1})\), up to the last low index
\(\lfloor(N-1)/2\rfloor\), its modulus is uniformly less than one:
\[
 \frac{|\cos^2(\pi(k+1/2)/N)-\sin^2(t/2)|}
      {\sin^2(\pi(k+1)/N)}
 \le\frac{7/20+6/25+o(1)}{13/20+o(1)}
       \longrightarrow\text{a value at most }59/65<1.
 \tag{17}
\]
The bounds \(\cos^2(3\pi/10)<7/20\),
\(\sin^2(3\pi/10)>13/20\), and
\(|\sin^2(t/2)|<6/25\) were used. Inequality (16) is applied
multiplicatively, so a Newton zero is retained and introduces no
division by a vanishing term. Both omitted low-index tails are
therefore bounded by a polynomial times their endpoint terms.
Formula (15) at the real endpoints and (12) give their strict
gap below \(\Re\psi\), uniformly on \(\mathcal B_0^2\).

For high indices, the
[complete Hermite estimates](../papers/circle-tree-volume/finite-bounds.tex)
give \(\|e_k\|_{\mathcal J}\le CN^a\). Full Hermite Fourier
interpolation gives the same polynomial bound on the entire real
angular period. The trigonometric Bernstein inequality consequently
gives, for every such \(k\),
\[
 |e_k(-2\cos t)e_k(-2\cos u)|
       \le CN^a e^{N(|\Im t|+|\Im u|)}
       \le CN^a e^{N/100}.
 \tag{18}
\]
To compare this with the selected phase, the
[edge Hessian bound](research_edge_hessian_and_phase_response.md),
Corollary 6, makes \(\Re\psi\) convex along every imaginary segment
in the larger box \(|\Re t|\le1,|\Im t|\le1/3\).
Its first derivative on the real slice vanishes. Real evenness and
\(-\psi_t(t,u)\le\pi^{-1}\tan(t/2)\le2t/(3\pi)\) for
\(0\le t,u\le1\) imply
\[
 \Re\psi(t,u)\ge\psi(\Re t,\Re u)
 >M_\infty-\frac2{3\pi}
 >\frac{112}{99}-\frac29=\frac{10}{11}.
 \tag{19}
\]
Here \(G>8/9\), \(3<\pi<22/7\), and
\(\sec^2(1/2)<4/3\) suffice. Thus the entire high half is
exponentially negligible, including both parities and all its zeros.
This finishes the full-kernel proof.

All estimates have strict reserve on compact sets. They persist
on a slightly enlarged parameter rectangle and wire rectangle,
which justifies the claimed neighborhood and the differentiated
remainders by Cauchy's estimate. At the simple odd boundary root,
no artificial normal is inserted into a quotient: (2) and (14)
are the original ordinary boundary polynomials from the start.

## 4. The original bounded meridian insertion

For a fixed \(R<1\), the same proof permits the original edge
insertion \(H_N(s)/W_k(s)\), uniformly for \(|s|\le R\).
Its exact interpolation is
\[
 I_N(x,s)=\frac{G_N(Nx)^2}{G_N(Nx-s)G_N(Nx+s)}
      =1-\frac{\pi s^2}{N}\cot(\pi x)+O_R(N^{-2}).
 \tag{20}
\]
The original finite estimates bound this insertion uniformly at
every omitted index, including its inverse. On the retained contour
it is holomorphic with (20). Thus the inserted kernel divided by
the bare kernel is
\[
 1-\frac{\pi s^2}{N}\cot(\pi x_*(t,u))+O_R(N^{-2}).
 \tag{21}
\]
Any separately prescribed physical-turn scalar is retained outside
this ratio. The insertion statement does not change a meridian,
replace a first normal, or assert an asymptotic for a subsequent
multi-vertex contraction. It supplies the uniform original edge
packet on the explicit domain (1).

The [scalar checker](../experiments/check_bare_kernel_thin_rectangle_constants.py)
verifies 33 strict inequalities above using exact fractions and
Taylor-series remainder bounds. Its
[record](../repro/results/research-bare-kernel-thin-rectangle.json)
contains every rational margin and the script and note hashes.
It checks the numerical constants in the proof; it is not a
sampled test of the uniform kernel assertion.

## 5. The expansion at imaginary heights up to three tenths

The small imaginary height in (1) is unnecessary. In this section put
\[
 \mathcal B_1=\{t:|\Re t|\le1,\ |\Im t|\le3/10\},\qquad
 a=1/10,\quad b=3/10,\quad h=3/100.
 \tag{22}
\]
The letters \(a,b\) in this section denote endpoints of the wire
interval; \(b(x,t)\) still denotes the phase in (3).

**Theorem 2.** The expansion (4), with its original nonzero
amplitude and normalization, holds uniformly on a neighborhood of
\(\mathcal B_1^2\). It has all the holomorphic remainder and
derivative properties stated in Theorem 1.

This is a theorem about the complete finite edge sum (2).
In particular, it estimates the kernel on the horizontal and
vertical trace contours whose real angles have magnitude at most
one. It does not cover angles between one and \(\pi/2\), and
does not by itself establish a whole-path source theorem.

### 5.1. The critical point stays in one regular factorial strip

Write \(c=\cos t\), \(d=\cos u\), \(U=1+\Re c\),
\(V=1+\Re d\), \(\beta=\Im c\), and \(\delta=\Im d\).
On \(\mathcal B_1^2\),
\[
 27/50<\Re c,\Re d<523/500,\qquad
 |\beta|,|\delta|<129/500.
 \tag{23}
\]
For the quantity \(C\) in (5) there are useful exact identities:
\[
 \begin{split}
 \Re C&=1-\frac{UV}{U+V}
 -\frac{(V\beta-U\delta)^2}
 {(U+V)((U+V)^2+(\beta+\delta)^2)},\\
 \Im C&=-\frac{\beta|1+d|^2+\delta|1+c|^2}
 {|2+c+d|^2}.
 \end{split}
 \tag{24}
\]
The correction on the first line is nonnegative and is less
than \((129/500)^2/(77/25)\). For the second line use
\[
 \frac{|1+c|^2+|1+d|^2}{|2+c+d|^2}
 =\frac12+\frac{|c-d|^2}{2|2+c+d|^2}
 <\frac12+
 \frac{(253/500)^2+(129/250)^2}{2(77/25)^2}.
\]
It follows that
\[
 -9/200<\Re C<23/100,\qquad |\Im C|<7/50.
 \tag{25}
\]
If \(2\pi x_*=\theta+i\nu\) on the principal inverse-cosine
branch, then \(\cos\theta=\Re C/\cosh\nu\) and
\(|\sinh\nu|=|\Im C|/\sin\theta\). Thus \(\sin\theta>97/100\)
and
\[
 21/100<\Re x_*<13/50,\qquad |\Im x_*|<23/1000<h.
 \tag{26}
\]
For the last inequality use
\(|\nu|<14/97\) and \(\pi>157/50\).
On the real parameter square the stronger bounds
\(1/5<x_*\le1/4\) follow immediately from \(0\le C<23/100\).

Throughout the wire rectangle
\([a,b]+i[-h,h]\), the factorial arguments
\(1/2-x\pm t/(2\pi)\) have real parts in a fixed compact
subinterval of \((0,1)\). The same holds for \(x\).
Consequently (15) holds uniformly on this rectangle for every
parameter in \(\mathcal B_1^2\), through every fixed order.
The logarithmic critical equation is \(A_x(x_*,t,u)=0\):
its exponential is one by (5), and continuation from \(t=u=0\)
fixes its integer logarithmic charge on the connected box.

### 5.2. Endpoint gaps on the real wire

Put \(r=\Re t\), \(s=\Re u\). On the real parameter square,
\[
 A_{xx}(x,r,s)\le-8\pi,\qquad a\le x\le b.
 \tag{27}
\]
Indeed the cosine denominators in the paired tangent formula
are positive, and
\(\tan(\pi x+r/2)+\tan(\pi x-r/2)\ge2\tan\pi x\).
The cotangent terms in (10) then give (27).

At a real wire point, a vertical change in a parameter has
quadratic cost at most
\[
 \Re b(x,r+iH)-b(x,r)
 \le C_x(r)H^2,\qquad
 C_x(r)=\frac{\sin(2\pi x)}
 {4\pi(\cos(2\pi x)+\cos r)}.
 \tag{28}
\]
To see this, differentiate twice in \(H\). The real part of
each squared secant is at most its modulus, and that modulus
is at most the squared secant at real part \(r\). The first
real derivative at \(H=0\) vanishes. This proves (28) with
the displayed half of the real second derivative.

For \(a\le x\le b\) and \(|r|\le1\), \(C_x(r)\le C_b(r)\).
The inequality \(\cos r\ge1-r^2/2\), followed by the chord
bound for the resulting convex reciprocal function of \(r^2\),
gives
\[
 C_b(r)\le\frac{11}{100}+\frac{29}{100}r^2<\frac25.
 \tag{29}
\]
The endpoint constants used here are
\[
 \frac{\tan(3\pi/10)}{4\pi}<\frac{11}{100},
 \qquad
 \frac{\sin(3\pi/5)}
 {4\pi(1+\cos(3\pi/5)-1/2)}<\frac25.
\]
The edge Hessian estimate on the larger box
\(|\Re t|\le1,\ |\Im t|\le1/3\), cited in Section 3,
also gives
\(\Re\psi(t,u)\ge\psi(r,s)\).
Equations (28)--(29) therefore imply on the entire real wire
\[
 \Re A(x,t,u)-\Re\psi(t,u)<9/125.
 \tag{30}
\]

There is a strict gap at each endpoint. At \(a\), (27) and
the real critical-point bounds give a real gap greater than
\(4\pi/100\). Subtracting the cost \(9/125\) leaves more
than \(1/25\).

For \(b\), let
\(D(r,s)=\psi(r,s)-A(b,r,s)\), \(T_b=\tan(3\pi/10)\).
The exact edge derivative gives, for \(0\le r,s\le1\),
\[
 D_r=\frac1\pi\left[
   \operatorname{atanh}(T_b\tan(r/2))
   -\operatorname{arsinh}(\tan(r/2)\cos(s/2))\right]
 \ge\frac{T_b-1}{2\pi}\,r.
 \tag{31}
\]
All the arguments of \(\operatorname{atanh}\) are below one.
The last inequality uses
\(\operatorname{atanh}z\ge z\),
\(\operatorname{arsinh}z\le z\) for \(z\ge0\), and
\(\tan(r/2)\ge r/2\). Since \(D(0,0)\ge\pi/100\),
separate evenness yields
\[
 D(r,s)\ge\frac{\pi}{100}
                  +\frac{T_b-1}{4\pi}(r^2+s^2).
 \tag{32}
\]
Now \(T_b>11/8\), so the coefficient of \(r^2+s^2\)
on the right is greater than \(261/10000\), the corresponding
coefficient in the height cost from (29). The constant terms
leave more than \(1/100\). In particular
\[
 \Re A(a,t,u)<\Re\psi-1/25,\qquad
 \Re A(b,t,u)<\Re\psi-1/100.
 \tag{33}
\]

### 5.3. Separating the constant cotangent terms

Two bounds hold throughout the entire wire rectangle:
\[
          \Re A_{xx}<-6,\qquad |\Im A_x|<7/2.
 \tag{34}
\]
Here are elementary estimates establishing them. Each real
tangent argument in (10) lies between \(\pi/10-1/2\)
and \(3\pi/10+1/2\). A tangent with negative real part has
real part greater than \(-1/5\); a tangent with nonnegative
real part has nonnegative real part. Also
\(\Re\cot(\pi x)>7/10\) on the rectangle.
The bracket in (10) is consequently greater than
\(4(7/10)-4/5=2\), proving the first inequality.

For the second use
\[
 A_x=\sum_{v=t,u}
       \Log\frac{\cos(2\pi x)+\cos v}{2\sin^2(\pi x)}.
\]
Each numerator has real part greater than \(11/50\) and
imaginary part of magnitude less than \(9/20\). Its argument
therefore has magnitude less than \(9/8\).
Furthermore
\(|\arg\sin(\pi x)|<3/10\). All these are the branches
continued from the positive real factors. Their sum has
magnitude less than \(2(9/8)+4(3/10)=69/20<7/2\).
The elementary endpoint comparisons follow, respectively, from
\[
 \begin{split}
 \cos(3\pi/5)\cosh(3\pi/50)+\cos1&>11/50,\\
 \sinh(3\pi/50)+\sin1\,\sinh(3/10)&<9/20,\\
 \arctan\!\left(\cot(\pi/10)\tanh(3\pi/100)\right)&<3/10.
 \end{split}
\]

Let \(f_N(x)=B_N(x,t)B_N(x,u)\). Choose vertical sides
\(a_N,b_N\) on half-grid lines, with
\(a_N=a+O(N^{-1})\), \(b_N=b+O(N^{-1})\), enclosing exactly
the retained indices. The residue formula is
\[
 \sum_{a_N<k/N<b_N}f_N(k/N)
             =\frac N{2i}\oint f_N(x)\cot(\pi Nx)\,dx.
 \tag{35}
\]
Split the cotangent into its constant part
\(-i\,\operatorname{sgn}(\Im x)\) and the remainder.
The constant parts, including the vertical segments on their
respective half-rectangles, give exactly
\(N\int_{a_N}^{b_N} f_N(x)\,dx\), by Cauchy's theorem.
On a horizontal side the remainder is
\(O(e^{-2\pi Nh})\); on a vertical half-grid side its modulus
is at most \(2e^{-2\pi N|\Im x|}\).

The second bound in (34) gives
\[
 \Re A(x+iy,t,u)
        \le\Re A(x,t,u)+\tfrac72|y|.
 \tag{36}
\]
Thus every vertical remainder has the endpoint gap (33).
Every horizontal remainder has rate, relative to \(\Re\psi\),
at most
\[
 \frac9{125}-(2\pi-\tfrac72)\frac3{100}<-\frac1{100}.
 \tag{37}
\]
Rounding the half-grid endpoints retains a smaller fixed
positive gap for all sufficiently large \(N\).
This controls the actual nonconstant lattice modes even though
the unsplit vertical contour need not itself have a gap.

### 5.4. The leading integral and the omitted indices

Move the real integral in (35) to the horizontal segment through
\(x_*\). The first inequality in (34) gives a strict maximum
at \(x_*\), with Gaussian curvature bounded away from zero.
At either endpoint on this horizontal line the rate is strictly
smaller than \(\Re\psi\), by (26) and (34).
Along the connecting vertical segment the real phase is convex:
its second derivative is \(-\Re A_{xx}>6\).
Both of its endpoints have a gap, one by (33), the other by
horizontal concavity. Convexity bounds the whole connector by
the larger of those endpoint values. No endpoint integral
is therefore lost in the translation.

The local Gaussian calculation is now exactly the one in
Section 2. Its coefficient is \(+N\) times the wire integral,
and (15) gives the nonzero amplitude in (4).

It remains to restore every omitted original index.
Below \(a_N\), the consecutive multiplier (16) has modulus
uniformly greater than one: its real numerator has a positive
lower bound already at \(x=a\). Above \(b_N\), through the
last low index, it has modulus uniformly less than one, since
\[
 \cos^2(3\pi/10)<7/20,\quad
 \sin^2(3\pi/10)>13/20,\quad
 |\sin^2(t/2)|
 =\sin^2(r/2)+\sinh^2(\Im t/2)<13/50.
 \tag{38}
\]
The limiting upper ratio is at most
\((7/20+13/50)/(13/20)=61/65<1\).
Their finite sums are therefore bounded by a polynomial times
their endpoint terms, whose gaps are (33). This uses the
multiplicative recurrence and remains valid at an exact
Newton zero.

On the high half the full Hermite estimate and trigonometric
Bernstein inequality give rate at most
\(|\Im t|+|\Im u|\le3/5\). Equation (19), valid on the
larger phase box, gives \(\Re\psi>10/11\).
Thus the entire high half is also exponentially smaller.
All steps hold for both level parities. Every comparison has
a strict reserve on a compact set, so it persists on a
neighborhood of \(\mathcal B_1^2\). The normalized holomorphic
remainder and its fixed ordinary-color derivatives follow
by Cauchy's estimate, including at ramified angular endpoints.
This proves Theorem 2. \(\square\)

The [large-height scalar check](../experiments/check_bare_kernel_large_height_constants.py)
verifies the endpoint comparisons used in this section with
outward interval arithmetic and exact rational arithmetic.
Its [saved record](../repro/results/research-bare-kernel-large-height.json)
contains the margins and dependency hashes. The contour identities,
uniform estimates and reconstruction of the finite sum are the
written arguments above.

## 6. The full rectangle through real angle pi over two

Put
\[
 \mathcal B_2=\{t:|\Re t|\le\pi/2,\ |\Im t|\le3/10\},
 \qquad a=1/10,\qquad h=1/25.
 \tag{39}
\]

**Theorem 3.** The original full kernel has expansion (4) on a
neighborhood of \(\mathcal B_2^2\), with the same nonzero
amplitude, normalization, both level parities, and all fixed
holomorphic remainder orders and ordinary boundary derivatives.
In particular it satisfies
\[
 |K_N(t,u)|\le CN^{-3/2}e^{N\Re\psi(t,u)}
                     \quad(t,u\in\mathcal B_2)
 \tag{40}
\]
for all sufficiently large levels. No term of the original finite
sum is replaced by a positive surrogate in this assertion.

We use the following three parameter patches. By evenness and
interchange of the two arguments, it suffices to take
\(r=\Re t\ge0\), \(s=\Re u\ge0\), with either sign of
each imaginary part:
\[
 \begin{array}{c|c|c|c}
  \text{patch}&r&s&b\\ \hline
  0&[0,23/20]&[0,23/20]&3/10\\
  1&[11/10,7/5]&[0,7/5]&27/100\\
  2&[27/20,\pi/2]&[0,\pi/2]&49/200.
 \end{array}
 \tag{41}
\]
The patches and their interchanges cover the whole square. Their
right endpoints satisfy \(b+\max(r,s)/(2\pi)<1/2\), with
margin at least \(1/200\). Thus every factorial argument in (14)
is in its regular real-part strip throughout
\([a,b]+i[-h,h]\), for all parameters in its patch.

### 6.1. A common critical strip and phase lower bound

Write \(c=\cos t,d=\cos u\), and retain the exact critical
quantity \(C=(1-cd)/(2+c+d)\). On this larger box,
\[
 0\le\Re c,\Re d<523/500,
 \qquad |\Im c|,|\Im d|<31/100.
 \tag{42}
\]
Use the harmonic-mean identities (24), now with
\(1\le U,V<1023/500\). Their nonnegative real correction
is less than \((31/100)^2/2\). For the imaginary part use
\[
 \frac{|1+c|^2+|1+d|^2}{|2+c+d|^2}
 \le\frac12+
       \frac{(21/20)^2+(31/50)^2}{8}.
\]
Consequently
\[
 -3/40<\Re C\le1/2,\qquad |\Im C|<3/14.
 \tag{43}
\]
If \(2\pi x_*=\theta+i\nu\), its principal inverse cosine
therefore has \(\sin\theta>6/7\), \(|\nu|<1/4\), and
\[
 1/6\le\Re x_*<53/200,
 \qquad |\Im x_*|<1/(8\pi)<h.
 \tag{44}
\]
For the real upper bound use
\(\sin(3\pi/100)>3/40\). Thus the saddle is below the
right endpoint on patches 0 and 1. On patch 2 one also has
\(\cos r<11/50\), hence \(U<5/4\), whereas \(V<41/20\).
The same exact real identity gives
\[
 \Re C>1-\frac{205}{264}-\frac1{20}>\frac16.
\]
As \(\cosh\nu<11/10\), this implies
\(\cos\theta>5/33>\sin(\pi/25)\), and therefore
\(\Re x_*<23/100<49/200\). These estimates locate the
critical point inside the regular factorial strip before using
its critical action.

The exponential critical equation is one by its defining algebra.
All critical factorial arguments have positive real part by (41)
and (44). Connected continuation from the complete point therefore
fixes its logarithmic charge to zero and identifies its critical
value with the original \(\psi\). The phase-only accretivity
lemma on the wide rectangle, Lemma 5 of
[the mixed-current note](research_path_mixed_trace_currents.md#9-vertical-current-monotonicity-at-powers-of-at-least-seven),
uses the exact edge Hessian, independently of any finite-kernel
expansion. It gives imaginary convexity and hence
\[
 \Re\psi(t,u)\ge\psi(r,s)\ge\psi(\pi/2,\pi/2)
 >M_\infty-\frac{4(1-1/\sqrt2)}\pi>\frac{19}{25}.
 \tag{45}
\]
For the middle inequality decrease both real arguments to their
largest values. Along the diagonal,
\(d\psi(v,v)/dv=-2\operatorname{asinh}(\sin(v/2))/\pi\).
Integrating \(\operatorname{asinh}z\le z\) proves the next
inequality. The last uses \(M_\infty>29/25\),
\(1/\sqrt2>7/10\), and \(\pi>3\).

### 6.2. Real-wire endpoints and the maximum between them

The fixed-patch
[endpoint lemma](research_bare_kernel_wide_endpoint_gaps.md)
proves for each right endpoint in (41)
\[
                  \Re A(b,t,u)<\Re\psi(t,u)-1/10000.
 \tag{46}
\]
Its outward certificate treats 48 products of parameter-boundary
sides. Separate harmonicity of \(\Re(A-\psi)\) proves the
inequality inside each full complex parameter rectangle; this is
not a sampled test of four real parameters. The phase branches and
critical factorial strip are checked in that lemma.

The left endpoint has an elementary bound. On the real regular
wire interval, the paired tangent formula gives \(A_{xx}\le-8\pi\).
The real critical point is at least \(1/6\), so the real left
endpoint loses at least \(4\pi/225\). At a fixed real wire point,
the vertical parameter cost is (28). At \(a=1/10\),
\[
 C_a(r)\le\frac{\tan(\pi/5)}{4\pi}<\frac1{4\pi}
                   \qquad(0\le r\le\pi/2).
\]
Both parameter heights together cost less than \(9/(200\pi)\).
Equation (45) and \(\pi>3\) give
\[
                  \Re A(a,t,u)<\Re\psi(t,u)-23/600.
 \tag{47}
\]

For the nonconstant cotangent modes we need a bound between the
endpoints, not only (46)–(47). We claim
\[
 \max_{a\le x\le b}\Re A(x,t,u)-\Re\psi(t,u)<3/50.
 \tag{48}
\]
If the maximum is at an endpoint, (46)–(47) suffice. Otherwise
put \(q=\cos(2\pi x)\) at an interior maximum. Its derivative
equation is exactly
\[
                     |q+c|\,|q+d|=(1-q)^2.
 \tag{49}
\]
Let \(C_0=\cosh(3/10)<523/500\). For \(-1\le q<0\),
convexity in \(v=\cos r\in[0,1]\), and monotonicity in
\(|\Im t|\), give
\[
 |q+\cos t|^2\le
       \max\{(q+C_0)^2,\ q^2+C_0^2-1\}.
 \tag{50}
\]
Both terms are strictly smaller than \((1-q)^2\) if
\(q<(1-C_0)/2\). For the second term use \(C_0^2<11/10\);
for the first, \(q+C_0>0\) on this interval. Equation (49)
therefore forces \(q>-23/1000\).

Write \(X=q+\cos r\), \(Y=q+\cos s\). The exact identity
for the height increment gives
\[
 |q+c|^2-X^2
 =2q\cos r\{\cosh(\Im t)-1\}+\sinh^2(\Im t)
 <\frac{1+|q|}{10},
 \qquad |q+d|\le |q|+523/500.
 \tag{51}
\]
For \(-23/1000\le q\le1/4\), (49) implies
\[
 X^2>
 \frac{(3/4)^4}{(1/4+523/500)^2}-\frac18>\frac1{16}.
\]
Since \(X\ge q>-1/4\), this gives \(X>1/4\); the same
holds for \(Y\). For \(q>1/4\) these inequalities are immediate.
Thus the real wire point is in the regular real-parameter chamber,
and the vertical parameter costs satisfy
\[
 C_x(r)+C_x(s)
 =\frac{\sqrt{1-q^2}}{4\pi}
       \left(\frac1X+\frac1Y\right)<\frac2\pi<\frac23.
 \tag{52}
\]
At this same point \(A(x,r,s)\le\psi(r,s)\) by real regular
concavity. The height cost is at most
\((3/10)^2\{C_x(r)+C_x(s)\}<3/50\), whereas
\(\Re\psi(t,u)\ge\psi(r,s)\). This proves (48).

### 6.3. The exact lattice modes

Every numerator \(\cos(2\pi x)+\cos t\) has positive real
part on the complex wire rectangle of its patch. On patches 0 and 1,
where \(\cos(2\pi b)<0\), a lower bound is
\(\cos(2\pi b)\cosh(2\pi h)+\cos R\), where \(R\)
is the patch's largest real parameter. Use, respectively,
\[
 \cos(23/20)>2/5,\quad -\cos(3\pi/5)<31/100,
 \qquad
 \cos(7/5)>1/6,\quad \sin(\pi/25)<22/175,
\]
together with \(\cosh(2\pi/25)<26/25\).
On patch 2 use \(\cos(2\pi b)+\cos R>0\) instead: both
real terms are nonnegative, and the first is bounded away from zero.
Also throughout the rectangle
\(|\arg\sin(\pi x)|<3/8\): use
\(\cot(\pi/10)<31/10\), \(\tanh(\pi/25)<22/175\),
and \(\tan(3/8)>39/100\).
The exact logarithmic derivative therefore obeys
\[
                         |\Im A_x|<\pi+3/2.
 \tag{53}
\]
These are the continued original branches: the numerators remain
in the right half-plane and \(\Re\sin(\pi x)>0\).

The horizontal curvature has a uniform bound as well. In (10)
at most one tangent in each pair has negative real part. Its real
argument is greater than \(-3\pi/20\), so its real part exceeds
\(-3/5\). All other tangent real parts are nonnegative because
their arguments have real part less than \(\pi/2\).
Moreover \(\Re\cot(\pi x)>7/10\) on this rectangle.
For the latter comparison the minimum is at \(x=3/10+ih\);
use \(\sin(3\pi/5)>19/20\) and the bounds just listed.
It follows that
\[
                          \Re A_{xx}<-8\pi/5.
 \tag{54}
\]

Use the exact half-grid residue contour (35), with sides tending
to \(a,b\) and heights \(\pm h\). Split its cotangent as in
Section 5.3. Its constant pieces, including their portions of the
vertical sides, are exactly \(N\int_{a_N}^{b_N}f_N(x)\,dx\).
Every vertical remainder retains its endpoint gap, by (46), (47),
(53), and the penalty \(2\pi|\Im x|\).
Every horizontal remainder has upper rate, relative to \(\Re\psi\),
less than
\[
 \frac3{50}-(\pi-3/2)\frac1{25}<-\frac1{200}.
 \tag{55}
\]
Here \(\pi>25/8\). Half-grid rounding preserves smaller fixed
gaps at all sufficiently large levels.

Move the remaining real integral to the horizontal through \(x_*\).
By (44) the saddle lies inside that rectangle, and (54) gives its
unique strict real maximum and nonzero Gaussian curvature. At each
horizontal endpoint the rate is lower by horizontal concavity.
The vertical connecting segment is bounded by its two endpoints,
because its second height derivative is \(-\Re A_{xx}>0\).
One endpoint has (46) or (47), and the other has the horizontal
concavity gap. Thus no connector is lost. The coefficient remains
exactly \(+N\) times the wire integral, and the original factorial
expansion (15) gives amplitude (4).

### 6.4. Every original omitted index

Below \(a_N\), the real numerator in each consecutive multiplier
(16) is uniformly positive and its modulus exceeds one, since
\(\Re c,\Re d\ge0\) and \(\cos(\pi/5)>4/5\).
Their omitted sum is bounded by its endpoint at polynomial cost,
and (47) supplies the gap.

Above the right endpoint, use the product multiplier rather than
bound its two factors separately. For real \(q\in[-1,1]\) set
\[
 P(q)=(1-q)^4-|q+c|^2|q+d|^2.
 \tag{56}
\]
The quartic terms cancel. Its cubic, quadratic and linear coefficients
satisfy
\[
 a_3\le-4,\qquad -3/5<a_2\le6,\qquad a_1\le-4.
\]
These follow from \(\Re c,\Re d\ge0\) and
\(|c|^2,|d|^2<11/10\). Hence
\[
                         P'(q)\le-14/5
                       \quad(-1\le q\le1/10).
 \tag{57}
\]
At each patch endpoint \(q_b=\cos(2\pi b)\), the limiting
product multiplier is strictly less than \(3/5\). Here are
bounds sufficient to verify this independently of the endpoint
phase certificate.

On patch 0, convexity in \(\cos r\in[0,1]\) shows
\(|q_b+c|,|q_b+d|<3/4\), so the ratio is at most
\(225/676<3/5\). On patch 1,
\(-3/20<q_b<-1/10\), and \(\cos r<1/2\) for the first
parameter. Convexity gives \(|q_b+c|<11/20\), while
\(|q_b+d|<6/5\), giving ratio at most \(66/121<3/5\).
On patch 2, \(0<q_b<1/25\) and \(\cos r<1/4\).
Thus \(|q_b+c|<9/20\), \(|q_b+d|<109/100\), and the
ratio is less than
\((9/20)(109/100)/(24/25)^2<3/5\).
In each calculation the modulus squared is a convex quadratic in
\(\cos r\); its maximum height is \(3/10\).

Since \(q_b<1/10\), these bounds imply
\(P(q_b)>(16/25)(9/10)^4\). Equations (56)–(57) and
\((1-q)^4\le16\) then give, for all \(q\le q_b\),
\[
 \frac{|q+c|^2|q+d|^2}{(1-q)^4}
       <1-\frac{6561}{250000}<\left(\frac{99}{100}\right)^2.
 \tag{58}
\]
The actual finite recurrence has midpoint and endpoint offsets
\(O(N^{-1})\), with denominator bounded away from zero on this
range. Its product multiplier is therefore less than \(199/200\)
uniformly for all sufficiently large levels. The omitted low-index
tail, through \(\lfloor(N-1)/2\rfloor\), is bounded by a
constant times its endpoint term. Equation (46) supplies its gap.
This multiplicative argument also retains an exact Newton zero;
there is no division by a vanishing Newton polynomial.

Finally the complete radical Fourier bound gives the whole high
half, including its first normals, at rate at most
\(|\Im t|+|\Im u|\le3/5\). Equation (45) supplies a
strict gap greater than \(4/25\). Every original index has now
been restored. The full Gaussian expansion follows through both
parities. All inequalities have strict reserves on a finite compact
cover; the same argument works on a neighborhood of the box.
Holomorphy, separate evenness and Cauchy's estimates give every
fixed ordinary-color derivative, including the ramified angles.
This proves Theorem 3. \(\square\)

The exact scalar margins in this section are checked by
[check_bare_kernel_wide_rectangle.py](../experiments/check_bare_kernel_wide_rectangle.py),
with the
[saved record](../repro/results/research-bare-kernel-wide-rectangle.json).
The independent endpoint interval certificate is linked in (46).
The scalar checks and the endpoint certificate have distinct scopes;
the written cotangent decomposition proves the original-sum coefficient.
