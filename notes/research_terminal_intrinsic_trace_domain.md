# A common trace domain for every terminal filling

Research note, 3 November 2026.

The terminal phases have a larger common analytic domain than the
small disks used in their quantum asymptotic theorems. In a trace
coordinate, their selected internal meridians are inverse branches
of real-rooted polynomials. This proves a uniform domain and a
contraction inequality without assuming that the peripheral period
itself is a Pick function.

The result concerns the already selected geometric phase germs.
It does not continue the quantum asymptotic expansion to the whole
domain. In particular, it supplies no deformation of the original
finite-source cycle. The last section identifies a limitation of a
possible use in short-chain composition.

## 1. The original stationary equation

For a positive integer \(p\ge2\), let \(t_p(u)\) be the selected
terminal critical point, initially for \(u\) near zero. Its equation
and boundary period are
\[
 \operatorname{arsinh}\!\left(\tan(t_p/2)\cos(u/2)\right)
       =i(pt_p/2-\pi),\qquad
 \mathcal U_p(u)=
 2\operatorname{arsinh}\!\left(\tan(u/2)\cos(t_p/2)\right).
 \tag{1}
\]
These are the original equations in
[the terminal phase calculation](research_terminal_period_pick_obstruction.md),
with \(\mathcal U_p=-2\pi W_p'\). A separately specified carrier
adds its prescribed linear imaginary term; none is suppressed here.

Write \(T_j,U_j\) for the standard Chebyshev polynomials:
\[
 T_j(\cos z)=\cos(jz),\qquad
 U_{j-1}(\cos z)\sin z=\sin(jz).
 \tag{2}
\]
Define
\[
 P_p(k)=kU_{p-1}(k),\qquad
 y=\cos(u/2),\qquad w=iy,\qquad k=\cos(t_p/2).
 \tag{3}
\]
Taking the hyperbolic sine of (1) and cancelling
\(\sin(t_p/2)\) gives the exact algebraic equation
\[
                         P_p(k)=w.
 \tag{4}
\]
Indeed, \(\sinh(i(pt_p/2-\pi))=-i\sin(pt_p/2)\), so that
\(y=-ikU_{p-1}(k)\). Below the chosen branch has nonreal \(k\);
thus the cancellation introduces no zero denominator.

All the roots of \(P_p\), counted with multiplicity, are real:
they are zero together with
\(\cos(j\pi/p)\), \(1\le j<p\). Zero is repeated when \(p\) is
even. Its leading coefficient is \(2^{p-1}>0\), and its largest
root is \(r_p=\cos(\pi/p)\).

## 2. The selected inverse branch

Let \(\mathbb H=\{w:\Im w>0\}\). List the \(p\) roots of \(P_p\)
as \(r_1,\ldots,r_p\), with multiplicity, and set
\[
 \Theta_p(k)=\sum_{\nu=1}^{p}\arg(k-r_\nu),
 \qquad \Im k>0,\qquad 0<\arg(k-r_\nu)<\pi.
 \tag{5}
\]
The subscripts in this root list do not indicate their ordering.
Let
\[
 \mathcal D_p=\{k:\Im k>0,\ 0<\Theta_p(k)<\pi\}.
 \tag{6}
\]

**Theorem 1.** The restriction \(P_p:\mathcal D_p\to\mathbb H\)
is a conformal bijection. Its inverse \(K_p\) takes values in the
first quadrant. The original selected germ is
\[
             \cos(t_p(u)/2)=K_p(i\cos(u/2)).
 \tag{7}
\]
Consequently it extends holomorphically to the entire strip
\[
                        \mathcal S=\{u:|\Re u|<\pi\}.
 \tag{8}
\]
On this strip the continued angle satisfies
\[
                0<\Re t_p(u)<\pi,\qquad \Im t_p(u)<0.
 \tag{9}
\]

*Proof.* For fixed \(\Im k=v>0\),
\[
 \frac{\partial\Theta_p}{\partial\Re k}
   =-\sum_{\nu=1}^{p}\frac{v}{|k-r_\nu|^2}<0.
 \tag{10}
\]
Its limits as \(\Re k\) tends to \(+\infty\) and \(-\infty\)
are \(0\) and \(p\pi\). Thus \(\mathcal D_p\) is the connected
region to the right of the unique continuous curve
\(\Theta_p=\pi\). The symmetry of the roots gives
\(\Theta_p(iv)=p\pi/2\). Hence every point of \(\mathcal D_p\)
has positive real part, also when \(p=2\).

The derivative \(P_p'\) has only real roots, by Rolle's theorem,
including the multiplicities inherited from repeated roots.
Thus \(P_p\) has no critical point in the upper half-plane.
Its restriction to \(\mathcal D_p\) is a proper local
biholomorphism into \(\mathbb H\): the roots of \(P_p(k)=w\)
stay bounded when \(w\) stays in a compact set, and they cannot
approach the real axis or a boundary curve of (6) while
\(\Im w\) stays positive. Its image is therefore both open
and closed in \(\mathbb H\). It is nonempty, so it is all
of \(\mathbb H\). A proper unramified covering of the simply
connected half-plane has degree one on each connected component.
This proves the asserted bijection.

It remains to identify the original selected root, rather than
an arbitrary inverse branch. At the complete boundary write
\(t_p(0)=2a-2ib\). The original terminal cone equations give
\[
                  0<a<\pi/p,\qquad b>0.
 \tag{11}
\]
See [the terminal geometry proof](research_terminal_powers_three_and_above.md)
and, for \(p=2\),
[the direct terminal theorem](research_two_crossing_terminal_filling.md).
Along \(k(v)=\cos(a-iv)\), \(0\le v\le b\), one has
\(\Re k(v)>\cos(\pi/p)\). The factorization
\[
 P_p(\cos(a-iv))
   =\cos(a-iv)\frac{\sin(p(a-iv))}{\sin(a-iv)}
 \tag{12}
\]
computes the continuously lifted argument in (5). The arguments
of its three factors lie respectively in
\([0,\pi/2)\), \((-\pi/2,\pi/2)\), and \((-\pi/2,0]\).
The middle bound uses \(0<pa<\pi\).
Thus at \(v=b\) the lifted argument is less than \(3\pi/2\).
It is positive by (5), and (4) at \(u=0\) says that it is
\(\pi/2\) modulo \(2\pi\). It is therefore exactly \(\pi/2\).
The selected root belongs to \(\mathcal D_p\).

Finally \(\Re\cos(u/2)>0\) on (8), so \(i\cos(u/2)\)
belongs to \(\mathbb H\). The first-quadrant inverse \(K_p\)
has the unique inverse cosine \(a-ib\) with
\(0<a<\pi/2\), \(b>0\). This inverse is holomorphic there
and proves (7)--(9). \(\square\)

The same construction for \(p\le-2\) is obtained by conjugating
the original coefficients:
\[
 t_{-p}(u)=-\overline{t_p(\overline u)},\qquad
 \mathcal U_{-p}(u)=\overline{\mathcal U_p(\overline u)}
 \quad(p\ge2).
 \tag{13}
\]

## 3. Logarithmic periods and a contraction inequality

The extension in Theorem 1 retains the unexponentiated equation.
To see this explicitly, the Chebyshev identity gives
\[
 1+\tan^2(t_p/2)y^2=T_p(k)^2.
 \tag{14}
\]
Neither \(T_p(k)\) nor \(k\) vanishes in the first quadrant.
The right side of (1), continued using (9), is therefore a
holomorphic lift of the inverse hyperbolic sine in its left
side. It agrees with that lift near zero, where the original
equation is known. The identity theorem fixes the same
logarithmic equation throughout \(\mathcal S\).

There is also a formula for the other peripheral period that
does not use an unspecified inverse-hyperbolic-sine branch:
\[
 \boxed{\displaystyle
 \exp(\mathcal U_p(u)/2)
   =\frac{k}{y}\left(\sin(u/2)-T_p(k)\right).}
 \tag{15}
\]
The square root entering this formula is
\[
 \sqrt{1+k^2\tan^2(u/2)}=-\frac{kT_p(k)}{y}.
 \tag{16}
\]
At \(u=0\), the complete stationary equation implies
\(kT_p(k)=-1\), so (16) has value one. This also follows
from \(\cosh(i(pt_p/2-\pi))=-T_p(k)\) and
\(\cosh(\operatorname{arsinh}\tan(t_p/2))=1/k\) on the
selected complete branch.
The identity
\[
 k^2 T_p(k)^2=y^2+k^2(1-y^2)
 \tag{17}
\]
proves (16) everywhere by continuation. It implies that
the right side of (15) is zero-free. Since \(\mathcal S\)
is simply connected, its logarithm with value zero at the
origin defines the original odd period on the whole strip.

The inverse is a Pick function in the intrinsic variable
\(w=i\cos(u/2)\). Its square is also a Pick function,
because \(K_p\) takes values in the first quadrant.
Schwarz's lemma, applied after the Möbius maps that take a
chosen source point and its image to zero in the unit disk,
therefore gives the explicit inequality
\[
 \boxed{\displaystyle
 \frac{2|K_p(w)|}{|P_p'(K_p(w))|}
       \le \frac{\Im(K_p(w)^2)}{\Im w}
       =\frac{2\Re K_p(w)\Im K_p(w)}{\Im w}.}
 \tag{18}
\]
No bound on \(p\) occurs. This is a contraction for the
hyperbolic metrics of the two half-planes, not a Euclidean
contraction on all of \(\mathcal S\).

For \(p=2\), \(K_2(w)^2=w/2\), so equality holds in (18).
For every \(p\ge3\), the inequality is strict at every point.
Indeed equality in Schwarz's lemma at one point would make
\(K_p^2\) a half-plane automorphism. But on the positive
imaginary ray, the rightmost inverse branch satisfies
\[
 K_p(iR)^2
   =2^{-2(p-1)/p}(iR)^{2/p}(1+o(1))
                    \qquad(R\longrightarrow\infty).
 \tag{18a}
\]
It is unbounded and grows sublinearly when \(p>2\).
A real Möbius automorphism of the half-plane either has a
finite limit at infinity or is affine with positive slope.
Neither behavior agrees with (18a). This proves strictness.
There is no uniform factor less than one on all of
\(\mathbb H\): at a real target \(w_0=P_p(k_0)\) with
\(k_0>r_p\), the inverse extends through the real axis with
positive derivative, and the ratio of the two sides of
(18) tends to one as \(w\to w_0\) from above.

The coordinate is a trace coordinate with a specified square
root. If the original boundary spectral coordinate is
\(c=-2\cos u\), then
\[
                    w^2=(c-2)/4,\qquad
             -2\cos t_p=2-4K_p(w)^2.
 \tag{19}
\]
The choice \(\Im w>0\) is part of the branch. A gluing or
turn must transport this coordinate and branch; (18) does
not authorize replacing its actual boundary map by an
arbitrary half-plane self-map.

## 4. The full-strip accretivity test fails already at power three

An additional inequality
\(\Re\mathcal U_p'(u)>0\) on all of \(\mathcal S\)
would have been useful for composing short fillings.
It is false, despite (18). This can be seen without a
numerical sample.

For \(p=3\),
\[
                  P_3(k)=4k^3-k.
 \tag{20}
\]
Put
\[
 k_c=\frac1{2\sqrt3},\quad
 c=\frac1{3\sqrt3},\quad
 h=\operatorname{arsinh}c,\quad
 u_c=\pi-2ih,\quad
 u_\varepsilon=u_c-\varepsilon,\quad \varepsilon>0.
 \tag{21}
\]
These points approach the boundary of \(\mathcal S\)
from its interior. At \(u_c\), \(y=ic\) and
\(P_3(k_c)=-c\), \(P_3'(k_c)=0\).
On the inverse branch in Theorem 1, Taylor expansion gives
\[
 \begin{split}
 i\cos(u_\varepsilon/2)
      &=-c+\tfrac i2\cosh h\,\varepsilon+O(\varepsilon^2),\\
 k(u_\varepsilon)
      &=k_c+
         e^{i\pi/4}\frac{7^{1/4}}{3\sqrt2}\sqrt\varepsilon
         +O(\varepsilon).
 \end{split}
 \tag{22}
\]
The positive square root is selected by (6): it approaches
the rightmost real inverse branch at its first critical point.

Differentiate (15), or equivalently differentiate the
inverse hyperbolic sine with the root (16). This yields
\[
 \mathcal U_p'(u)
  =\frac{k/y^2-i(1-y^2)/(yP_p'(k))}
         {-kT_p(k)/y}.
 \tag{23}
\]
At (21), \(T_3(k_c)=-4c\),
\(-k_cT_3(k_c)/(ic)=-2i/\sqrt3\), and
\(\cosh^2h=28/27\). Substitution of (22) into (23) gives
\[
 \mathcal U_3'(u_\varepsilon)
    =-\frac{7^{3/4}}{\sqrt6}\,
           e^{i\pi/4}\varepsilon^{-1/2}+O(1).
 \tag{24}
\]
In particular,
\[
       \Re\mathcal U_3'(u_\varepsilon)
        =-\frac{7^{3/4}}{2\sqrt3}\varepsilon^{-1/2}+O(1)
                     \longrightarrow-\infty.
 \tag{25}
\]
Adding any real carrier multiple \(i\gamma u\) leaves this
real part unchanged.

Thus the real-rooted inverse coordinate gives an actual
common analytic domain and the contraction (18), while the
peripheral response does not remain accretive on that
whole domain. This does not rule out a smaller domain
adapted to reduced continued-fraction chains. Proving
that such a domain is preserved by their actual boundary
maps, and reducing the full original quantum cycle to it,
remain separate requirements. The theorem above alone
does not estimate the currents created in that reduction.

## 5. Reproduction

Run
~~~sh
python3 experiments/check_terminal_intrinsic_domain.py \
  --precision 110 \
  --output repro/results/research-terminal-intrinsic-domain-root.json
~~~
The [checker](../experiments/check_terminal_intrinsic_domain.py)
continues the selected inverse from the complete root and verifies
its lifted argument after each step. It reduces the step if a numerical
Newton iteration switches branches near a boundary critical value.
At powers \(2,3,4,5,8,15,30\), it checks 42 inverse values, the
real-root factorization, the half-plane contraction, and 21 exact
period identities. Five further values approach the cubic fold
in (21) and test the coefficient in (24).

The [saved record](../repro/results/research-terminal-intrinsic-domain-root.json)
contains the script hash and precision. These are finite checks of
the formulas and branch conventions. The global domain and
contraction statements follow from the proof above.
