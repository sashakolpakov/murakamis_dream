# Cancelling the long lower contour by its complementary arc

Research lemma, 2 November 2026. The lower-\(x\) correction in the
adjacent two-crossing sum cannot be estimated absolutely on the first
proposed contour. There is nevertheless an exact cancellation available
after changing variables to \(w=e^{-2\pi ix}\). The interpolation
has a small, explicit failure of periodicity. Removing that factor
produces a holomorphic differential at \(w=0\); its long circular
arc can then be replaced by the oppositely oriented short arc.

This note proves that replacement, bounds its error, and estimates
the new short arc on a specified \(y\)-contour. It does not move the
original \(y\)-contour to that contour, nor estimate the original
endpoint and corner currents. Those remain separate parts of the
finite sum.

## 1. The exact differential near the lower end

Let \(f_N(x,y;u)\) be the exact interpolating summand of
[the adjacent pair](research_adjacent_two_crossing_pair.md), and put
\[
 w=e^{-2\pi ix},\quad Y=e^{2\pi iy},\quad
 Q=e^{2\pi i/N},\quad
 R_N(w,y)=\frac{1-(w/Y)^N}{(1-w^N)^3}.
 \tag{1}
\]
All logarithms below are their power-series branches at \(w=0\).
The [exact cyclotomic gauge](research_adjacent_pair_cyclotomic_gauge.md)
gives
\[
 f_N(x,y;u)e^{-2\pi iNx}
   =C_N(y,u)\,w\,\exp\{\Phi_N(w,y)\}\,R_N(w,y)^x,
 \tag{2}
\]
where
\[
 C_N(y,u)=iN e^{-i\pi/(6N)}
     e^{N(i\pi y^2-i\pi/6)}
       \frac{\mathcal B_N(y,u)}{G_N(Ny)^2},
 \tag{3}
\]
and
\[
\begin{aligned}
 \Phi_N(w,y)={}&y\log(1-(w/Y)^N)\\
 &-\frac1N\sum_{k=0}^{N-1}k
       \{\log(1-wQ^k/Y)-3\log(1-wQ^k)\}\\
 &+\frac{i}{2\pi N}
       \{\operatorname{Li}_2((w/Y)^N)-3\operatorname{Li}_2(w^N)\}.
\end{aligned}
\tag{4}
\]
Here \(\mathcal B_N(y,u)\) is the exact Newton interpolation,
equal to \(e_j(-2\cos u)\) when \(y=j/N\).
Formula (2) includes the affine offsets and crossing phase of the
original finite summand.

The lower correction kernel in the one-sided lattice formula is
\[
 \frac{e^{-2\pi iNx}}{1-e^{-2\pi iNx}}
                         =\frac{w^N}{1-w^N}.
 \tag{5}
\]
Since \(dx=-dw/(2\pi iw)\), its full integrand is therefore
\[
 f_N(x,y;u)\frac{e^{-2\pi iNx}}{1-e^{-2\pi iNx}}\,dx
  =-\frac{C_N(y,u)}{2\pi i}
      \frac{e^{\Phi_N(w,y)}}{1-w^N}R_N(w,y)^x\,dw.
 \tag{6}
\]
This retains the complete rational kernel, not merely its first
Fourier term.

After deleting \(R_N^x\), the right-hand side is a single-valued
holomorphic differential on
\[
                    |w|<\min(1,|Y|).
 \tag{7}
\]
There is no pole at \(w=0\). This is the cancellation that would
be lost by separately taking absolute values on the two rays
approaching that point.

## 2. Uniform bounds at a fixed radius

Let \(y\) vary in a fixed compact set and let \(u\) vary in a small
complex disk. Write
\[
 \mu=\min\{1,\inf_y|Y|\}>0,\qquad
 0<r<\mu/2,\qquad \rho=r/\mu<1/2.
 \tag{8}
\]
For \(|w|\le r\), the series for \(\log(1-z)\) gives
\[
              |\log R_N(w,y)|\le C\rho^N.
 \tag{9}
\]
Here and below the constants are independent of \(N\).

Define
\[
 \phi(w,y)=\frac{i}{2\pi}
       \{3\operatorname{Li}_2(w)-\operatorname{Li}_2(w/Y)\}.
 \tag{10}
\]
Then the exact formula (4) satisfies
\[
                  \Phi_N(w,y)=N\phi(w,y)+O(\rho),
 \tag{11}
\]
uniformly on the disk in (8).

To verify (11), put
\[
 \ell(t)=\log(1-we^{2\pi it}/Y)-3\log(1-we^{2\pi it}).
 \]
The middle line of (4) is
\(-\sum_{k=0}^{N-1}(k/N)\ell(k/N)\).
Both \(\ell\) and its first \(t\)-derivative are \(O(\rho)\);
the elementary Riemann-sum error is thus \(O(\rho)\). Expanding
the convergent logarithm series and using
\[
 \int_0^1 t e^{2\pi imt}\,dt=\frac1{2\pi im}
       \quad(m\ge1)
 \]
shows that
\(-\int_0^1t\ell(t)\,dt=\phi(w,y)\).
The first and last lines of (4) are \(O(\rho^N)\), which proves
(11). In particular
\[
                 |\Phi_N(w,y)|\le C N\rho.
 \tag{12}
\]

For \(y\) on a fixed regular strip and \(u\) near zero, the
canonical factorial and Newton expansions give
\[
 C_N(y,u)=\frac{i}{4N\sin^2\pi y}
               e^{NV(y,u)}(1+O(N^{-1})),
 \tag{13}
\]
where
\[
 V(y,u)=b(y,u)-2J(y)+i\pi y^2-\frac{i\pi}{6}.
 \tag{14}
\]
The factor \(e^{-i\pi/(6N)}\) in (3) is part of the relative
error in (13), not an omitted exponential normalization.
At \(u=0\),
\[
             V(y)=-6J(y)+J(2y)+i\pi y^2-\frac{i\pi}{6}.
 \tag{15}
\]

## 3. Complementary-arc replacement

Fix \(y\), \(r\), and two real numbers \(a<b<a+1\). Put
\(H=-\log r/(2\pi)\). The line from \(a-iH\) to \(b-iH\)
maps to one clockwise arc of the circle \(|w|=r\).
The other arc, oriented from the same first endpoint to the
same second endpoint, is obtained by letting \(x\) run from
\(a-iH\) to \(b-1-iH\). It has the opposite angular direction.

**Lemma.** In the lower correction integral, the first arc can
be replaced by the second with an error bounded by
\[
 C_r N^A
  \exp N\{\Re V(y,u)+C\rho+\log\rho\}.
 \tag{16}
\]
The constants are uniform when \(a,b\) range in a bounded set,
when \(y,u\) range as in Section 2, and when \(b-a\) stays
between zero and one. The external factor \(N\) from the
one-sided lattice formula, if included, only changes \(A\).

**Proof.** For the differential obtained from (6) by deleting
\(R_N^x\), the two arc integrals are exactly equal. Their
difference is an integral around the full circle, and the
differential is holomorphic on its disk by (7).

On either chosen lift of the two arcs,
\[
 |x|\le C_r,\qquad
 |R_N(w,y)^x-1|\le C_r\rho^N.
 \tag{17}
\]
The latter follows from (9); the fixed depth \(H\) causes no
dependence on \(N\). Also
\[
 |1-w^N|^{-1}\le(1-r^N)^{-1}\le C_r.
 \]
The arc lengths are at most \(2\pi r\). Equations (6),
(12)--(13), and (17) bound the error of ungauging the two arcs
by a polynomial in \(N\) times
\(e^{N(\Re V+C\rho)}\rho^N\), proving (16).
\(\square\)

In particular, for any fixed target rate \(T\), the error is
below \(e^{N(T-\delta)}\) for some \(\delta>0\) once \(r\)
is sufficiently small, uniformly on the specified compact set.
Indeed \(C\rho+\log\rho\to-\infty\). The radius is fixed
before \(N\to\infty\); no estimate at an \(N\)-dependent
infinite depth is being used.

The expression on the new arc still has to be bounded. The
lemma alone does not make it small.

## 4. A contour on which the new short arc is small

Set
\[
 h_\infty=\frac{\log2}{4\pi},\qquad
 Y_\infty=\frac{1+i\sqrt7}{4},\qquad
 y_\infty=\frac{\log Y_\infty}{2\pi i},\qquad
 M_\infty=\Re V(y_\infty).
 \tag{18}
\]
The logarithm has argument in \((0,\pi/2)\).
The unexponentiated equation \(V'(y_\infty)=0\) is verified
in Section 4 of
[the lattice-transfer note](research_adjacent_pair_lattice_transfer.md).
The [Bloch--Wigner identity](research_adjacent_alias_bloch_identity.md)
proves \(M_\infty=M\), where \(M\) is the original finite
critical action. That comparison uses the actual logarithmic
branches and fixes the real constant.
At \(y=a+ih_\infty\), \(0<a<1/2\), direct differentiation gives
\[
 \Re V''(y)
  =-4\pi\Re\cot(\pi y)-2\pi\Re\tan(\pi y)<0.
 \tag{19}
\]
Both real parts are positive because \(\sin(2\pi a)>0\).
Thus \(\Re V(a+ih_\infty)\) is strictly concave and has its
unique maximum \(M_\infty\) at \(\Re y_\infty\).

For the original triangular cutoff let \(\epsilon=10^{-6}\),
as in the tail theorem. Its \(x\)-interval at real \(y\)-coordinate
\(a\) is, up to half-grid displacement,
\[
                  [\epsilon,1-a-\epsilon].
 \tag{20}
\]
The complementary arc in Section 3 has angles
\[
          -2\pi\epsilon\le\arg w\le2\pi(a+\epsilon).
 \tag{21}
\]
Its orientation is irrelevant for the following absolute bound.
The same bound holds after sufficiently small endpoint
perturbations, including the actual \(O(N^{-1})\) displacements.

On the interval \(I=[1/6,1/4]\), which contains
\(\Re y_\infty\), put \(Y=e^{2\pi i(a+ih_\infty)}\).
For \(0\le\theta\le2\pi a\),
\[
 \Im\{(3-Y^{-1})e^{i\theta}\}
    =3\sin\theta+\sqrt2\sin(2\pi a-\theta).
 \tag{22}
\]
The right-hand side is positive and concave as a function of
\(\theta\). Its minimum is therefore at one of the two
endpoints, and is at least \(\sqrt6/2\).
Its derivative has absolute value at most \(3+\sqrt2<5\).
Consequently it is at least \(1\) on the slightly extended
angle range (21), for every \(a\in I\).

For \(w=re^{i\theta}\), \(r\le1/16\), the two dilogarithm tails
in (10) satisfy
\[
 \left|3\operatorname{Li}_2(w)-\operatorname{Li}_2(w/Y)
                           -(3-Y^{-1})w\right|
 \le \frac{3r^2}{4(1-r)}
           +\frac{2r^2}{4(1-\sqrt2r)}
 <2r^2.
 \tag{23}
\]
Combining (22)--(23) gives
\[
                    \Re\phi(w,y)\le-\frac{r}{4\pi}
                         \qquad(a\in I)
 \tag{24}
\]
on the complementary arc.

On the compact complement of the interior of \(I\) in
\([\epsilon,1/2-\epsilon]\), equation (19) gives a fixed
strict loss below \(M_\infty\). The bound
\(|\phi(w,y)|\le Cr\) there follows from its convergent series.
Choose \(r>0\) small enough that this cost is less than half
that loss. Equations (11), (13), and (24) now prove:

**Proposition.** There are fixed \(r,\delta>0\) such that the
complementary-arc integrals in (6), on
\[
 y=a+ih_\infty,\qquad
          \epsilon\le a\le1/2-\epsilon,
 \tag{25}
\]
are bounded by \(CN^A e^{N(M_\infty-\delta)}\), uniformly
in \(a\), through both level parities. The ungauging errors
from Section 3 satisfy the same bound after reducing \(r\)
if necessary. The estimate persists on small complex
neighborhoods of the fixed contours.

**Proof.** On \(I\), (24) gives the fixed loss
\(r/(4\pi)\); on its complement the preceding compactness
argument gives the fixed loss. The \(O(\rho)\) in (11)
costs only a bounded factor, since it is not multiplied
by \(N\). The fixed-length integrals and their lattice
prefactors are polynomial in \(N\). For the ungauging
errors use (16). All inequalities have slack, so small
complex perturbations preserve a smaller loss.
\(\square\)

This proposition treats the complete rational lower correction,
including all its Fourier modes. It does not rely on a finite
charge cutoff.

## 5. What remains before this applies to the original sum

The original principal surface uses the \(y\)-height
\(\log7/(4\pi)\). The new arc estimate uses
\(\log2/(4\pi)\). These heights cannot simply be interchanged
in the whole finite contour formula: a deformation introduces
connecting sides and corner currents. Those contributions must
still be estimated or cancelled in their original combination.
For example,
\[
       \Re V(ih)=2\pi h
 \]
on the canonical limiting branch. At the original height
\(h=\log7/(4\pi)\), this is \(\log7/2\), larger than the
selected finite-saddle rate. For an explicit comparison, the
finite saddle has
\(\Re x_*>\tfrac1{16}\), since
\(\sqrt7/5>1/2>\tan(\pi/8)\). The exact action formula
(17) and the dilogarithm upper bound (20) in the lattice-transfer
note, together with
\(69/100<\log2<7/10\) and \(19/10<\log7<2\), give
\[
 M<\frac{713}{1600}+\frac{293}{628}
                  <\frac{19}{20}<\frac{\log7}{2}.
 \tag{26}
\]
Thus a boundary estimate for the
new \(y\)-contour does not bound the whole intervening strip.

The separate Bloch--Wigner calculation proves
\(M_\infty=M\), so the short-arc proposition is a strict
bound below the selected finite rate. This real-action
identity gives no contour coefficient by itself, and does
not remove the connecting-current problem just described.

The gain established here is the cancellation of a long
lower circular arc with its complementary short arc, with
an explicit error at finite \(N\). The full transfer from
the original lattice still requires the remaining contour
assembly.
