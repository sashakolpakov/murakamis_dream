# The actual root half-twist and a far-color contour estimate

Private derivation, 1 November 2026. No repository source is changed.

The root crossing is treated through its exact values on the moving Casimir roots, rather than by a complex-strip estimate for its canonical interpolation polynomial. A paired-grid contour cancels the apparent complete-meridian singularity and retains the original ordinary-circle pivot. The result is a strict auxiliary-color loss when the remaining raw source has its proved angular Gaussian.

## 1. The physical root data

Let
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad
 \eta=(-1)^{N+1},\quad
 P_s(z)=\mathcal T_N(z)+2\cos(2\pi s),
 \tag{1}
\]
where \(\mathcal T_N(u+u^{-1})=u^N+u^{-N}\). The normalized polynomial trace is
\[
 \phi_s(F)=(-1)^dN^2[z^d]\operatorname{rem}_{P_s}F.
 \tag{2}
\]
The actual ordinary-circle operator, including its pivot sign, is
\[
 L_j(z)=(-1)^{j-1}U_{j-1}(z/2),\qquad
 L_j(-2\cos\tau)=\frac{\sin(j\tau)}{\sin\tau}.
 \tag{3}
\]
The quotient in (3) is its polynomial continuation at zeros of the denominator.

For the equal-color object with parameter \(s\), the actual checked crossing has scalar and stripped eigenvalues
\[
 \kappa_s=q^{(d+s)^2/2},\qquad
 \lambda_r=(-1)^r q^{r(r+1)}q^{-2sr},
 \qquad 0\le r<N.
 \tag{4}
\]
These are the physical crossing and its retained Cartan scalar. Define
\[
 a_s=\frac d2+s,\qquad
 \tau_r(s)=\frac{2\pi}{N}(a_s-r),\qquad
 z_r=-2\cos\tau_r(s).
 \tag{5}
\]
Then \(e^{iN\tau_r}=\eta e^{2\pi is}\), and the \(z_r\) are the roots of \(P_s\), with multiplicity at collisions.

For the prescribed logarithmic lift,
\[
 r^2+(N+1-2s)r=(r-a_s)^2-a_s^2+2Nr.
 \tag{6}
\]
The last summand contributes \(e^{2\pi ir}=1\). Therefore
\[
 \lambda_r=q^{-a_s^2}
       \exp\!\left(\frac{iN\tau_r(s)^2}{4\pi}\right).
 \tag{7}
\]
Multiplication by the physical scalar in (4) gives the exact formula
\[
 \boxed{\displaystyle
 (\kappa_s\lambda_r)^\epsilon
 =C_{N,\epsilon}(s)
       \exp\!\left(\frac{i\epsilon N\tau_r(s)^2}{4\pi}\right),
 \quad
 C_{N,\epsilon}(s)=q^{\epsilon(d^2/4-s^2/2)},}
 \tag{8}
\]
for \(\epsilon=0,\pm1\). In particular, no factor of modulus \(e^{cN}\) has been suppressed. The complete factor \(q^{\epsilon d^2/4}\) has modulus one, and \(C_{N,\epsilon}(s)\) and its inverse are uniformly bounded on every fixed \(s\)-disk.

The opposite equal-color orientation uses \(-s\); (8)'s scalar is even in \(s\). The two mixed reference orders use the full complete crossing polynomial \(r_0\), with the already specified bounded monodromy scalar on reversal. They are addressed by the constant-relation version at the end.

## 2. A paired-grid integral with no meridian denominator

Fix \(R<1/2\) and \(y>0\). Let \(\mathcal R_y\) be the positively oriented rectangle with real sides at \(-\pi,\pi\) and imaginary sides at \(-y,y\). For all sufficiently large \(N\), both grids \(\tau_r(s)\), \(\tau_r(-s)\), \(0\le r<N\), lie inside it uniformly on \(|s|\le R\). Their real endpoints stay strictly between \(-\pi\) and \(\pi\), since
\[
 |\operatorname{Re}\tau_r(\pm s)|
 \le\pi-\frac{\pi(1-2R)}{N}.
 \tag{9}
\]
Their imaginary parts are at most \(2\pi R/N<y\).

Let \(E_{N,s}\) be any raw polynomial, and put
\[
 B_{N,s,j}(\tau)
 =\sin(j\tau)
   \exp\!\left(\frac{i\epsilon N\tau^2}{4\pi}\right)
   E_{N,s}(-2\cos\tau).
 \tag{10}
\]
This function is odd in \(\tau\), even when its coefficients and \(s\) are complex. The exact contour identity is
\[
 \boxed{\displaystyle
 \phi_s(R_s^\epsilon L_jE_{N,s})
 =-\frac{N^2 C_{N,\epsilon}(s)}{2\pi i}
  \int_{\partial\mathcal R_y}
  B_{N,s,j}(\tau)\,
  \frac{e^{iN\tau}}
  {(e^{iN\tau}-\eta e^{2\pi is})
   (e^{iN\tau}-\eta e^{-2\pi is})}\,d\tau .}
 \tag{11}
\]
Here \(R_s^\epsilon\) means the actual full crossing polynomial, including the scalar of (4), raised to the indicated fixed power and interpreted in the original quotient. The product with \(E\) need not be reduced before using (11).

We prove the identity initially at generic \(s\). For \(u=e^{i\tau}\), the derivative at a root is
\[
 P_s'(-u-u^{-1})
 =\frac{2iN\sin2\pi s}{u-u^{-1}}
 =\frac{N\sin2\pi s}{\sin\tau}.
 \tag{12}
\]
Lagrange interpolation, (3), and (8) thus give
\[
 \phi_s(R_s^\epsilon L_jE)
 =\frac{\eta N C_{N,\epsilon}(s)}{\sin2\pi s}
       \sum_{r=0}^{N-1}B_{N,s,j}(\tau_r(s)).
 \tag{13}
\]

Introduce logarithmic-derivative kernels
\[
 K_{\pm s}(\tau)=
 \frac{iN e^{iN\tau}}{e^{iN\tau}-\eta e^{\pm2\pi is}}.
 \tag{14}
\]
Each has residue one at its grid. Since
\(\tau_{d-r}(-s)=-\tau_r(s)\), oddness of \(B\) implies
\[
 \sum_r B(\tau_r(s))
 =\frac1{4\pi i}
   \int_{\partial\mathcal R_y}B(\tau)
                   (K_s(\tau)-K_{-s}(\tau))\,d\tau.
 \tag{15}
\]
The difference is exactly
\[
 K_s-K_{-s}
 =-2\eta N\sin2\pi s\,
   \frac{e^{iN\tau}}
   {(e^{iN\tau}-\eta e^{2\pi is})
    (e^{iN\tau}-\eta e^{-2\pi is})}.
 \tag{16}
\]
Substitution in (13) proves (11), including its sign and its power \(N^2\).

There is no division by \(\sin2\pi s\) left in (11). Its contour contains no poles for \(|s|\le R\), once \(N\) is sufficiently large as in (9). Thus its right side is holomorphic through \(s=0\). The actual crossing polynomial has its established removable complete collision, including the full first normal coefficients. Analytic continuation proves (11) at completeness as well. It does not replace the full Hermite trace by values at a repeated root.

## 3. Uniform estimates for the contour kernel

Write
\[
 \mathcal K_{N,s}(\tau)=
 \frac{e^{iN\tau}}
 {(e^{iN\tau}-\eta e^{2\pi is})
  (e^{iN\tau}-\eta e^{-2\pi is})}.
 \tag{17}
\]
On either horizontal side, with \(\tau=t\pm iy\), the two root constants have moduli in \([e^{-2\pi R},e^{2\pi R}]\), while \(|e^{iN\tau}|=e^{\mp Ny}\). For sufficiently large \(N\),
\[
 |\mathcal K_{N,s}(t\pm iy)|\le C_R e^{-Ny}.
 \tag{18}
\]

On a vertical side \(\tau=\pm\pi+iv\), the exponential is
\(e^{iN\tau}=-\eta e^{-Nv}\). Put \(t=e^{-Nv}>0\). For
\(|\arg(e^{\pm2\pi is})|\le2\pi R<\pi\),
\[
 |t+e^{\pm2\pi is}|
 \ge \cos(\pi R)\bigl(t+|e^{\pm2\pi is}|\bigr)
 \ge c_R(t+1).
 \tag{19}
\]
It follows that
\[
 |\mathcal K_{N,s}(\pm\pi+iv)|
 \le C_R\frac{t}{(1+t)^2}
 \le C_Re^{-N|v|}.
 \tag{20}
\]
This bound includes \(v=0\); no unproved separation of individual roots is required there. The hypothesis \(R<1/2\) is used both in (9) and (19).

## 4. A strict far-color loss

Assume the raw remaining source has the fresh Gaussian bound
\[
 |E_{N,s}(-2\cos(t+iv))|
 \le N^K
 \exp N\{F-c t^2+C v^2+\epsilon_N\},
 \quad |t|\le\pi,\ |v|\le y_0,\ |s|\le R,
 \tag{21}
\]
where \(c>0\), \(C\ge0\), \(\epsilon_N\to0\), and all constants are uniform over the other physical auxiliary colors. A product of a fixed number of canonical outputs with their respective fresh Gaussians satisfies (21) at the sum of their assigned actions; no prior quotient reduction is needed.

The root crossing's Gaussian phase obeys
\[
 \left|\exp\!\left(\frac{i\epsilon N(t+iv)^2}{4\pi}\right)\right|
 =\exp\!\left(-\frac{\epsilon Ntv}{2\pi}\right)
 \le\exp\!\left(\frac{N|t v|}{2\pi}\right),
 \tag{22}
\]
and \(|\sin(j(t+iv))|\le e^{j|v|}\). Fix \(0<\delta<1\) and suppose
\[
 1\le j\le(1-\delta)N.
 \tag{23}
\]
On the horizontal sides of the rectangle, (18), (21), and (22) give exponent at most
\[
 F+\epsilon_N-c t^2+
       \frac{|t|y}{2\pi}+Cy^2-\delta y.
 \tag{24}
\]
Completing the square yields
\[
 -ct^2+\frac{|t|y}{2\pi}\le\frac{y^2}{16\pi^2c}.
 \tag{25}
\]
Set \(C_*=C+(16\pi^2c)^{-1}\), and choose a fixed positive
\[
 y\le y_0,\qquad C_*y^2\le\frac{\delta y}{2}.
 \tag{26}
\]
The horizontal exponent is then at most \(F-\delta y/2+\epsilon_N\).

On the vertical sides \(t=\pm\pi\), (20)--(23) give exponent at most
\[
 F-c\pi^2+C v^2+\frac{|v|}{2}
       -\delta|v|+\epsilon_N
 \le F-c\pi^2+Cy^2+\frac y2+\epsilon_N.
 \tag{27}
\]
Shrink \(y\) further so that
\[
 Cy^2+\frac y2\le\frac{c\pi^2}{2}.
 \tag{28}
\]
This is compatible with (26), since \(y\) is free to be any sufficiently small fixed number. The vertical exponent is then at most \(F-c\pi^2/2+\epsilon_N\).

The contour has bounded length. Its prefactor in (11), the source prefactor in (21), and the bounded scalar in (8) have only polynomial cost. Thus there is \(\gamma>0\), depending on the fixed source parameters, \(R\), and \(\delta\), such that
\[
 \boxed{\displaystyle
 \sup_{\substack{|s|\le R\\1\le j\le(1-\delta)N}}
 |\phi_s(R_s^\epsilon L_jE_{N,s})|
 \le\exp N(F-\gamma),
 \qquad \epsilon=0,\pm1,}
 \tag{29}
\]
for every sufficiently large \(N\), at both parities.

The same proof applies to the opposite-color root relation \(P_0\): use \(\sigma=0\) in the kernel and the complete crossing chirp, retaining the bounded mixed-order monodromy scalar. The actual typed turn ratios used to expose the root are bounded as well. The single primitive main-cut factor \(H_N(s)\) does not change the loss on the disk under consideration.

## 5. Scope

The conclusion is conditional on (21), with its original absolute action \(F\). It does not follow from a spectral norm bound for \(E\) alone. In the separated-bare-hub class, both the decorated outputs and the whole bare-hub outputs have a fresh Gaussian at their assigned intrinsic pressures; a raw root product then has (21) at their sum. The independent geometric accounting identifies that sum with the original complete augmented action when the indicated root is exposed.

This result controls a color separated from the complete color, uniformly in the other colors. It does not identify a filled knot's smaller critical action, prove a nonzero leading whole-source contribution, or establish the limiting regular main-meridian profile. It also does not claim the same contour proof on disks reaching \(|s|=1/2\), where its chosen unwrapped root interval meets its endpoints. No uniform complex-strip bound for the canonical crossing polynomial has been assumed.
