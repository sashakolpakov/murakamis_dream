# Canonical cutoff regularization and the uniform square-root node profile

Private written proof, 18 November 2026.

The Laurent resolution [L] regularizes finite primitives of the original
Borel source through its simple Alexander node. Combined with the exact
finite-Laplace current [B], this gives a canonical cutoff function
holomorphic through that node and a uniform square-root-scale connection
profile. All statements concern this cutoff function. No identification
with the original finite invariant or with a hyperbolic component is made.

## 1. Source, sheets, and the cutoff

Retain the actual source, node hypotheses, and constants of [L]:
\[
 z=Y-\alpha,\qquad r=\Delta_K'(\alpha)^{-1}\ne0,\qquad
 \eta_*=\frac B{2A}\ne0.
 \tag{1}
\]
Write \(\mathcal B(z,\xi)=\mathcal B_h\mathscr W(\alpha+z,\xi)\).
The convergent resolution is
\[
 \mathcal B(z,\xi)=\frac1w
       H\left(z,w,\frac{z^3}{w^2}\right),\qquad
 w^2=z^2-\xi/\eta_*,\qquad H(0,0,0)=r,
 \tag{2}
\]
where \(H\) is holomorphic on a fixed polydisk. Initially \(w=z\)
at \(\xi=0\). The continuation domain includes a \(w\)-annulus
whose inner radius is a constant times \(|z|^{3/2}\) and whose outer
radius is fixed and small. For small \(z\ne0\), the initial point \(w=z\)
lies in this annulus.

Fix a sufficiently small \(R\ne0\). Choose
\(\beta^2=-\eta_*\), and a square root \(\sqrt R\). On a fixed
small \(z\)-disk the two endpoint sheets are the holomorphic functions
\[
 w_{R,\pm}(z)^2=z^2-R/\eta_*,
 \qquad w_{R,\pm}(0)=\pm\frac{\sqrt R}{\beta}.
 \tag{3}
\]
For \(z\ne0\), continue from \(w=z\) to \(w_{R,\pm}(z)\) within
the annulus supplied by [L]. Its projection is an actual continued
Borel path from \(\xi=0\) to \(R\). Define the two canonical cutoffs
\[
 U_{R,\pm}(h,z)=\frac1h\int_{0}^{R}
                  e^{-\xi/h}\mathcal B(z,\xi)\,d\xi,
 \qquad h\ne0,
 \tag{4}
\]
with those endpoint sheets and histories.

These integrals depend only on the chosen endpoint in (3), not on
additional winding in the permitted \(w\)-annulus. In fact [L] gives
\[
 b_k(s)=\sum_{j=0}^k c_{kj}s^{-2j-1}
                  +\sum_{m=0}^{k-1}d_{km}s^m,\qquad
 \sum_j|c_{kj}|+\sum_m|d_{km}|\le CD^k,
 \tag{5}
\]
and \(w=zs\). Under \(d\xi=-2\eta_*w\,dw\), the negative powers of
the differential in (4) are even powers of \(w\). Multiplication
by \(e^{\eta_*w^2/h}\) preserves their parity and creates no \(w^{-1}\)
term. Normal convergence on closed subannuli makes its residue zero.
Thus it has a single-valued primitive on the annulus.
This observation retains the original source history while removing
an arbitrary winding choice on that resolved domain.

## 2. Finite primitives extend through the node

For each \(a\ge1\), let
\[
 P_{a,\pm}(z,R)=I_\xi^a\mathcal B(z,R)
 =\frac1{(a-1)!}\int_0^R(R-\xi)^{a-1}\mathcal B(z,\xi)\,d\xi
 \tag{6}
\]
along the same continued path. With \(w=w_{R,\pm}(z)\), substitution
in (5) gives the exact expression
\[
 P_{a,\pm}
 =-\frac{2\eta_*^a}{(a-1)!}
 \int_{t=z}^{w}(t^2-w^2)^{a-1}
 \left\{\sum_{k,j}c_{kj}z^{k+2j}t^{-2j}
       +\sum_{k,m}d_{km}z^{k-m-1}t^{m+1}\right\}dt.
 \tag{7}
\]
This formula initially holds for \(z\ne0\), termwise on annular paths.
All powers of \(z\) explicitly displayed outside the integral are
nonnegative.

Expand the factor \((t^2-w^2)^{a-1}\). In its term indexed by
\(0\le l<a\), a negative Laurent monomial has exponent \(2l-2j\).
Its primitive divides by \(2l-2j+1\), an odd nonzero integer.
The polynomial monomials divide by \(m+2l+2\), also nonzero.
Thus no logarithm occurs. After evaluation at the two endpoints,
the monomials have the following forms, up to their scalar coefficients:
\[
\begin{array}{ll}
 \text{negative part at }t=w:
       &w^{2a-1}z^{k-j}(z^3/w^2)^j,\\
 \text{polynomial part at }t=w:
       &z^{k-m-1}w^{m+2a},\\
 \text{either part at }t=z:
       &z^{k+2l+1}w^{2a-2-2l}.
\end{array}
 \tag{8}
\]
Every exponent of \(z\) is nonnegative. Since \(w_{R,\pm}\) is
holomorphic and nonzero on a fixed small disk, (5) proves that the
endpoint sums extend holomorphically through \(z=0\).
They are the extensions of the canonical primitives, not a choice of
new integration constants.

There is also a bound uniform in \(a\). Shrink the disk so that
\(|z|\le c|w|\), \(c<1\), while \(|w|^2\asymp|R|\), and all
arguments of \(H\) remain in a smaller fixed polydisk.
The denominators just described have modulus at least one.
The binomial coefficients in (7) sum to \(2^{a-1}\).
In the last line of (8), the factor \((z/w)^{2l}\) has modulus at
most one. Summing the coefficient bounds in (5) therefore gives
constants independent of \(a\):
\[
       |P_{a,\pm}(z,R)|
       \le C C_0^a\,\frac{|R|^{a-1/2}}{(a-1)!}.
 \tag{9}
\]
Here \(R\) is fixed; the disk and constants may be chosen after it.
The same conclusion for fixed \(z\)-derivatives follows on smaller
disks by Cauchy's formula.

Expand the exponential in (4) about its upper endpoint. The exact
result is
\[
 U_{R,\pm}(h,z)
       =e^{-R/h}\sum_{a\ge1}h^{-a}P_{a,\pm}(z,R).
 \tag{10}
\]
On the original finite path this is ordinary termwise integration
of an entire exponential. Bound (9) makes the right side normally
convergent for \(h\ne0\), locally uniformly with \(z\) on its full
disk. It proves that both canonical cutoffs extend jointly
holomorphically through \(z=0\) for every \(h\ne0\).
This extension is not holomorphy at \(h=0\).

## 3. The actual endpoint current is uniform through the node

Let \(\mathcal P(h)\) be the supplied actual analytic finite-shift
annihilator of the source, in the ordering retained in [B].
Shrink nested \(z\)-disks and the \(h\)-radius so that all its
shifts stay inside the larger disk of (10).
For \(z\ne0\), [B] gives the exact identity
\[
        \mathcal P(h)U_{R,\pm}(h,z)
                         =e^{-R/h}J_{R,\pm}(h,z),
 \tag{11}
\]
where the current is locally holomorphic at \(h=0\). Its finite-path
formula retains all coefficient and shift endpoint contributions.
Local paths with the same endpoint sheet give the same \(U\) by
Section 1, and hence the same \(J\) for \(h\ne0\). Their extensions
at \(h=0\) agree by uniqueness. Thus these are well-defined currents
on the punctured \(z\)-disk.

For \(h\ne0\), define \(J=e^{R/h}\mathcal P(h)U\) on the full
smaller \(z\)-disk, using (10). It is holomorphic there.
Choose a still smaller fixed circle \(|z|=\rho\). The local
extensions provided by [B] cover this compact circle; a finite
subcover supplies a common \(h\)-radius and bound.
For \(|z|<\rho\), the Cauchy integral
\[
 \widetilde J(h,z)=\frac1{2\pi i}
             \int_{|\zeta|=\rho}\frac{J(h,\zeta)}{\zeta-z}\,d\zeta
 \tag{12}
\]
is jointly holomorphic also at \(h=0\). For \(h\ne0\), Cauchy's
formula identifies it with the current already defined on the disk.
This proves a joint extension of (11), with a uniform bound
\[
                  |J_{R,\pm}(h,z)|\le C.
 \tag{13}
\]
All fixed \(z\)-derivatives obey the corresponding smaller-disk
bounds. The identity \(J_{R,\pm}(0,z)=0\), proved away from the
node in [B], also extends to the whole disk.

On a closed sector facing \(R\), so that
\(\Re(R/h)\ge c_R/|h|>0\), (11) is now a uniform exponentially
small absolute defect through \(Y=\alpha\). This is an actual
canonical cutoff regularization. It is not an exact homogeneous
solution or a relative error estimate for an arbitrary exterior source.

## 4. The uniform square-root-scale profile

Fix a closed \(h\)-subsector with
\[
        |\arg(R/h)|\le\frac\pi2-\delta,\qquad \delta>0,
 \tag{14}
\]
and choose its continuous square root so that
\(\sqrt R/\sqrt h\) lies in the right Gaussian decay sector.
Use the corresponding endpoint choices (3).
For \(s\) in any fixed compact subset of \(\mathbb C\), set
\[
                        z=\sqrt h\,s.
 \tag{15}
\]
Then, uniformly on that compact and on (14),
\[
 \sqrt h\,U_{R,\pm}(h,\sqrt h\,s)\longrightarrow
 y_\pm(s):=-2\eta_*r\,e^{-\eta_*s^2}
                 \int_s^{\infty_\pm}e^{\eta_*v^2}\,dv.
 \tag{16}
\]
The endpoint \(\infty_\pm\) lies in the decay sector containing
the ray \(\pm\mathbb R_+/\beta\). The Gaussian is entire, so this
integral is independent of finite path changes and of the ray
chosen within that sector.

Here is a direct proof preserving the finite cutoff. Changing variables
in (4), first to \(w\) and then to \(w=\sqrt h\,v\), gives
\[
\begin{split}
 \sqrt h\,U_{R,\pm}(h,\sqrt h\,s)
 ={}&-2\eta_*e^{-\eta_*s^2}
 \int_{v=s}^{v_{R,\pm}}
 e^{\eta_*v^2}
 H\left(\sqrt h\,s,\sqrt h\,v,
                   \frac{\sqrt h\,s^3}{v^2}\right)\,dv,\\
 &v_{R,\pm}=w_{R,\pm}(\sqrt h\,s)/\sqrt h.
\end{split}
 \tag{17}
\]
The formula is initially for \(s\ne0\); its value at \(s=0\) is
the holomorphic extension proved in Section 2.

Let \(|s|\le M\), and choose a fixed radius \(L>M+1\).
For \(s\ne0\), first move radially out from \(s\) to the circle
\(|v|=L\), then along that circle to the argument of \(v_{R,\pm}\),
and finally radially to the actual endpoint.
The compact portion has uniformly bounded length and satisfies
\(|v|\ge|s|\). Therefore
\[
 \left|\frac{\sqrt h\,s^3}{v^2}\right|
                         \le\sqrt{|h|}\,|s|.
 \tag{18}
\]
All three arguments of \(H\) tend uniformly to zero on this
compact portion. Its integrand converges uniformly to the Gaussian
times \(r\), including for arbitrarily small nonzero \(s\).
The bound (18) also keeps the path in the permitted annulus:
in the original \(w\)-coordinate its inner constraint is small
uniformly, even when the starting point approaches zero.

For small \(h\), uniformly in \(|s|\le M\),
\[
 \eta_*v_{R,\pm}^2=\eta_*s^2-R/h.
 \tag{19}
\]
Condition (14) puts the final ray in a strict Gaussian decay sector,
with a constant \(c>0\) such that
\(|e^{\eta_*v^2}|\le e^{-c|v|^2}\) along it.
The endpoint magnitude tends to infinity uniformly.
On this ray \(H\) stays bounded: \(|\sqrt h\,v|\le|w_{R,\pm}|\)
is fixed and small, and its other two arguments satisfy uniform
small bounds. For bounded \(v\) they tend to zero.

To justify the limit, fix a larger radius \(L_1\).
On the part with \(|v|\le L_1\), use the preceding uniform
convergence. Both the remaining source integral and the limiting
Gaussian integral have tails bounded by
\(C\int_{L_1}^{\infty}e^{-ct^2}dt\), independently of \(h,s\).
Let \(h\to0\), then \(L_1\to\infty\).
This proves uniform convergence for \(0<|s|\le M\).
Both sides are holomorphic in \(s\) through zero; continuity extends
the same uniform estimate to \(s=0\).
Path deformations used here preserve the canonical cutoff because
their differentials have zero annular residue, as proved in Section 1.
This proves (16) without an infinite-ray estimate at fixed \(z\ne0\).

## 5. The nonzero canonical connection coefficient and its scope

The two profiles satisfy the exact inhomogeneous transport
\[
                    A y_\pm'(s)+B s\,y_\pm(s)=B r.
 \tag{20}
\]
This follows by differentiating (16) and using
\(2A\eta_*=B\). The forcing \(Br\) is the original simple-pole
normalization; it has not been replaced by a freely chosen
homogeneous solution.

With the orientation from \(-\infty/\beta\) to \(+\infty/\beta\),
the elementary Gaussian integral gives
\[
 \begin{split}
 y_+(s)-y_-(s)
 &=-\frac{2\eta_*r\sqrt\pi}{\beta}\,e^{-\eta_*s^2}\\
 &=2\beta r\sqrt\pi\,e^{-\eta_*s^2}\ne0.
 \end{split}
 \tag{21}
\]
Thus the difference of the actual two canonical cutoff functions has
this nonzero leading coefficient in the uniform scaling (15).
On each fixed \(s\)-compact it is nonzero for all sufficiently
small \(h\) in (14), by (16) and the positive minimum of the modulus
of (21) there. More explicitly, on each such compact,
\[
 |U_{R,+}(h,\sqrt h\,s)-U_{R,-}(h,\sqrt h\,s)|
                                  \ge c_K|h|^{-1/2}.
 \tag{22}
\]
At the same time, their actual operator defects are uniformly
exponentially small by (11)--(14).

There is also a growing overlap with the quadratic action. Fix
\(0<\delta_1<1/6\), and allow \(|s|\le |h|^{-\delta_1}\).
The two lower endpoints in (17) cancel exactly. The resulting
endpoint-to-endpoint integral can be deformed onto its two opposite
Gaussian rays joined by an arc of a fixed radius \(\varepsilon>0\).
On this contour \(|v|\ge\varepsilon\), and
\[
 |z|\le |h|^{1/2-\delta_1},\qquad
 \left|\frac{\sqrt h\,s^3}{v^2}\right|
       \le\varepsilon^{-2}|h|^{1/2-3\delta_1}.
 \tag{23}
\]
These estimates keep the entire contour in the resolved annulus for
small \(h\); in particular its inner \(w\)-radius
\(\sqrt{|h|}\varepsilon\) is larger than a fixed multiple of
\(|z|^{3/2}\). The endpoint rays remain in strict decay sectors
uniformly on this growing range.

Holomorphy of \(H\) on a larger fixed polydisk gives the Lipschitz
bound
\[
 |H(z,\sqrt h\,v,\sqrt h\,s^3/v^2)-r|
 \le C\left(|z|+\sqrt{|h|}|v|
                       +\sqrt{|h|}|s|^3/|v|^2\right).
 \tag{24}
\]
The fixed arc has bounded length, and the three terms on the right
are integrable on the rays against their common Gaussian majorant.
For the constant Gaussian integral, replacing the finite endpoints
by infinity costs \(O(e^{-c/|h|})\).
Therefore, with \(C_* = 2\beta r\sqrt\pi\ne0\),
\[
 \sqrt h\,e^{\eta_*s^2}
       (U_{R,+}-U_{R,-})(h,\sqrt h\,s)
       =C_*+O(|h|^{1/2-3\delta_1})
       \quad (|s|\le |h|^{-\delta_1}).
 \tag{25}
\]
All constants are uniform on the closed sector (14).
The zero-residue argument in Section 1 justifies the deformation
also when the canceled lower endpoint is inside the fixed arc.

Let \(S\) be the local analytic classical action of [L], normalized
by \(S(\alpha)=0\) and \(S'(Y)=\log\ell(Y)/Y\) for its nonabelian
operator root. It satisfies
\(S(\alpha+z)=-\eta_*z^2+O(z^3)\).
Since \(z^3/h=O(|h|^{1/2-3\delta_1})\) in (25), the same statement
can be written
\[
 (U_{R,+}-U_{R,-})(h,z)
 =C_*h^{-1/2}e^{S(\alpha+z)/h}
       \{1+O(|h|^{1/2-3\delta_1})\},
 \quad |z|\le |h|^{1/2-\delta_1}.
 \tag{26}
\]
In particular this includes shrinking overlap sequences with
\(|z|/\sqrt{|h|}\to\infty\), while \(h/z^2\to0\) and \(z^3/h\to0\).
The use of \(S\) here is justified by that last smallness condition;
it is not a proof of transport to a fixed nonzero \(z\), or of the
full moving Borel singular curve.

This is a local source connection for the canonical finite-cutoff
functions. It is not a determination of the full moving Borel
singular curve \(\xi=-S(Y)\), a fixed-\(z\) leading exponential,
an infinite Laplace sum, or a physical root-of-unity scalar.
The operator component has not been identified with the hyperbolic
representation component. The broad arbitrary-short-filling target,
including knots with \(\Delta_K=1\), is unchanged.

## 6. Complete proof sources

| Label | Complete source | SHA256 |
|---|---|---|
| L | notes/research_classical_verma_borel_laurent_resolution.md | 6a65d3f47544255c46e6cc5450d822b5b38cfccce591e5ad59e21d4c569be341 |
| B | notes/research_canonical_borel_finite_laplace_current.md | b3b1e4246e2b5ed1b364585b8504edf8e0f1f1e15797f62f276fc4b89dca586f |

L supplies the actual convergent Laurent resolution and its source
normalization. B supplies the exact finite-cutoff operator current
on common meridian charts away from the node. The primitive extension,
joint current regularization, scaled profile and its coefficient
are proved above. No external proof or mathematical program is used.
Frozen proofs and public manuscripts are unchanged.
