# Complex-color reciprocity with the original normal correction

Private written proof, 17 November 2026. The entire finite
Fourier--Hermite interpolation of an original signed twist is exactly
a sum of \(2|p|\) Gaussian functions and one fixed-contour Mordell
integral. The correction vanishes in the value transform at integer
color, but its derivative generally remains in the normal transform.
The formula holds at every level \(N\ge2\), without a coprimality or
parity restriction.

The integer-color real reciprocity in
[the full-Hermite reciprocity note](research_full_hermite_gauss_reciprocity.md)
cannot itself be continued by retaining its bounded sawtooth:
its omitted factor becomes \(e^{-2\pi i z}\). The present contour
formula retains that factor. It represents the entire interpolation
already specified in
[the coherent Gaussian source](actual_coherent_filling_gaussian_chirp.md);
it does not define an ordinary module of nonintegral color.

## 1. Original normalization and the entire formula

Fix
\[
 N\ge2,\qquad d=N-1,\qquad q=e^{\pi i/N},\qquad Q=q^2,\qquad
 \kappa=q^{d^2/2},\qquad t_j=(j+\tfrac12)/N.
 \tag{1}
\]
The displayed logarithm defines every fractional power. Let
\(p\in\mathbb Z\setminus\{0\}\), and put \(\sigma=\operatorname{sgn}p\).
The original value and eigenlog-normal data are
\[
 h_j=Q^{pj(j+1)}
     =\kappa^{-p}e^{2\pi i pN(t_j-1/2)^2},
 \qquad d_j=2pN(t_j-\tfrac12)h_j.
 \tag{2}
\]
Their specified entire transforms are
\[
 H(z)=\frac1N\sum_{j=0}^{N-1}h_j e^{-2\pi i zt_j},\qquad
 D(z)=\frac1N\sum_{j=0}^{N-1}d_j e^{-2\pi i zt_j},
 \qquad
 \mathfrak a(z)=\frac{D(z)+(N-z)H(z)}N.
 \tag{3}
\]
Only \(a_n=\mathfrak a(n)\), \(0\le n<N\), are the canonical
Chebyshev coefficients. These data include the original repeated-node
normals and the odd simple node.

Orient the line
\[
 L_\sigma=e^{i\sigma\pi/4}\mathbb R
 \tag{4}
\]
by increasing real parameter. Define
\[
 F_z(t)=e^{2\pi i pN(t-1/2)^2-2\pi i zt},\qquad
 r(z)=e^{-2\pi i z},\qquad
 \mathcal M_p(z)=\int_{L_\sigma}
             \frac{F_z(t)}{1+e^{2\pi i Nt}}\,dt.
 \tag{5}
\]
This is an absolutely convergent integral, not a principal value.
The line meets the real axis only at \(0\), away from every pole.
Set
\[
 I_p=\{\min(0,2p),\ldots,\max(0,2p)-1\},
 \tag{6}
\]
\[
 \mathcal G_p(b)=
  \frac{e^{i\sigma\pi/4}}{\sqrt{2|p|N}}
       e^{-\pi i b-\pi i b^2/(2pN)},\qquad
 S_p(z)=\sum_{k\in I_p}(-1)^k\mathcal G_p(z-Nk).
 \tag{7}
\]
The square root in the denominator is the positive real square root.

**Theorem 1.** For every \(z\in\mathbb C\),
\[
 \boxed{
 H(z)=\kappa^{-p}
       \left[r(z)S_p(z)+\sigma(1-r(z))\mathcal M_p(z)\right].}
 \tag{8}
\]
All terms are entire in \(z\), and the original normal and coefficient
interpolations are
\[
 \boxed{
 D(z)=\frac{ipN}{\pi}H'(z)-pNH(z),\qquad
 \mathfrak a(z)=\frac{ip}{\pi}H'(z)
                         +(1-p-z/N)H(z).}
 \tag{9}
\]
Thus (8)--(9) retain every original first normal. There is no division
by a possibly vanishing Gauss sum.

In particular, at every integer \(n\),
\[
 H(n)=\kappa^{-p}S_p(n),
 \tag{10}
\]
\[
 \boxed{
 D(n)=\kappa^{-p}\left[
   \sum_{k\in I_p}(-1)^k(2pN+n-Nk)\mathcal G_p(n-Nk)
                  -2|p|N\mathcal M_p(n)\right],}
 \tag{11}
\]
\[
 \boxed{
 \mathfrak a(n)=\kappa^{-p}\left[
   \sum_{k\in I_p}(-1)^k(1+2p-k)\mathcal G_p(n-Nk)
                  -2|p|\mathcal M_p(n)\right].}
 \tag{12}
\]
Equation (12) is a coefficient formula for the original twist only
when \(0\le n<N\). The normal correction in (11) is not eliminated
by the integer-color specialization in (10).

## 2. Fixed-contour proof, including negative powers

Write \(e_\sigma=e^{i\sigma\pi/4}\). On \(t=e_\sigma y\),
\[
 \operatorname{Re}\bigl(2\pi i pN(t-\tfrac12)^2-2\pi i zt\bigr)
   =-2\pi|p|Ny^2+2\pi\operatorname{Im}
                         (e_\sigma(pN+z))\,y.
 \tag{13}
\]
The denominator in (5) is uniformly separated from zero on this
line. More precisely,
\[
 \left|1+e^{2\pi iNt}\right|^{-1}\le C_*,
 \qquad C_*=(1-e^{-\pi/2})^{-1}.
 \tag{14}
\]
To see this, put \(v=2\pi N\operatorname{Im}t\). On the tilted line
\(|2\pi N\operatorname{Re}t|=|v|\). If \(|v|\le\pi/2\), the
cosine of the real argument is nonnegative, so the denominator has
modulus at least \(1\). If \(|v|>\pi/2\), use
\(\left|1-|e^{2\pi iNt}|\right|\), on either side of the real axis.
Equations (13)--(14), also after multiplication by any fixed power
of \(t\), prove absolute convergence locally uniformly in \(z\).
They justify differentiation under the integral of every order
and prove that \(\mathcal M_p\) is entire.

Consider the parallelogram with long sides
\(L_\sigma\cap\{|y|\le R\}\) and its translate by \(1\).
Traverse the first side in its prescribed direction and the
translated side in the opposite direction. This orientation is
clockwise when \(\sigma=1\) and counterclockwise when \(\sigma=-1\).
The enclosed real poles are exactly \(t_j\), \(0\le j<N\), with
\[
 \operatorname{Res}_{t=t_j}
     \frac{F_z(t)}{1+e^{2\pi iNt}}
       =-\frac{F_z(t_j)}{2\pi iN}.
 \tag{15}
\]
The two short sides have \(t=\pm Re_\sigma+u\), \(0\le u\le1\).
Their Gaussian modulus is
\(\exp[-2\pi|p|NR^2+O_{N,p,z}(R+1)]\), uniformly in \(u\);
their denominator reciprocals are bounded for sufficiently large
\(R\). Hence both integrals tend to zero. The residue theorem gives
\[
 \kappa^pH(z)=\sigma\left[
     \int_{L_\sigma}\frac{F_z(t)}{1+e^{2\pi iNt}}\,dt
    -\int_{L_\sigma+1}\frac{F_z(t)}{1+e^{2\pi iNt}}\,dt
                         \right].
 \tag{16}
\]
This fixes the sign for both powers.

The centered shift has no additional scalar:
\[
 F_z(t+1)=r(z)e^{4\pi i pNt}F_z(t).
 \tag{17}
\]
For \(E=e^{2\pi iNt}\), the finite Laurent identity is
\[
 \frac{1-E^{2p}}{1+E}
       =\sigma\sum_{k\in I_p}(-1)^kE^k.
 \tag{18}
\]
For \(p>0\) this is polynomial division of \(1-E^{2p}\).
For \(p<0\), multiplication by \(E^{-2p}\) reduces it to that
same identity; thus the negative-index range in (6) and the sign
in (18) are essential. Substituting (17) into (16), and using
\[
 \frac{1-rE^{2p}}{1+E}
       =\frac{1-r}{1+E}
                      +r\frac{1-E^{2p}}{1+E},
 \tag{19}
\]
leaves the Mordell term in (8) and \(2|p|\) ordinary Gaussian
integrals.

For every complex \(b\), completing the square gives
\[
 \int_{L_\sigma}
       e^{2\pi i pN(t-1/2)^2-2\pi i bt}\,dt
       =\mathcal G_p(b).
 \tag{20}
\]
Indeed the constant after completing the square is
\(-\pi ib-\pi ib^2/(2pN)\). The translated tilted line may be
moved back to \(L_\sigma\), since the integrand is entire and its
two connecting tails decay quadratically. On that line the
remaining integral is
\[
 e_\sigma\int_{\mathbb R}e^{-2\pi|p|Ny^2}\,dy
       =e_\sigma/\sqrt{2|p|N}.
 \tag{21}
\]
Equations (16)--(21) prove (8).

Finally differentiate the literal finite sum (3). Since
\(\partial_z e^{-2\pi izt}=-2\pi it e^{-2\pi izt}\), this gives
(9) directly from (2), without a reconstruction of missing
normals. At integer \(n\), \(r(n)=1\) but \(r'(n)=-2\pi i\).
Consequently the derivative of the Mordell term contributes
\(-2pN\sigma\mathcal M_p(n)\) to \(D(n)\). Also
\[
 \mathcal G_p'(z-Nk)
   =-\pi i\left(1+\frac{z-Nk}{pN}\right)
                              \mathcal G_p(z-Nk).
 \tag{22}
\]
These facts give (10)--(12), including their signs and factors.

## 3. The contour translation retains its residues

The fixed contour in (5) is part of the formula. Its later
translation has an explicit cost. For real \(a<b\) which are not
half-grid points, let
\[
 \mathcal M_{p,c}(z)=
   \int_{L_\sigma+c}\frac{F_z(t)}{1+e^{2\pi iNt}}\,dt
                    \quad(c=a,b).
 \tag{23}
\]
Each integral is entire in \(z\). Repeating the same parallelogram
argument proves
\[
 \boxed{
 \mathcal M_{p,a}(z)-\mathcal M_{p,b}(z)
   =\frac{\sigma}{N}
       \sum_{\substack{j\in\mathbb Z\\
                       a<(j+1/2)/N<b}}
                         F_z((j+\tfrac12)/N).}
 \tag{24}
\]
The sum is finite. Reversing \(a,b\) reverses its orientation.
Differentiating (24) gives every corresponding normal residue,
with no interchange problem. The case \(a=0,b=1\) is (16).
Other crossings can involve half-grid aliases outside the
physical window, which remain the literal terms in (24).
Thus moving the line to pass through a proposed saddle does not
permit deleting the crossed residues.

## 4. Full original operator and finite color endpoints

Put \(E_0(Z)=1\) and \(E_n(Z)=2T_n(Z/2)\) for \(n\ge1\).
The full-Hermite source theorem identifies
\[
 f_{N,2p}(Z)=\sum_{n=0}^{N-1}a_nE_n(Z),\qquad
 R^{2p}=\kappa^{2p}f_{N,2p}(\Omega)
 \tag{25}
\]
for the original pair Casimir \(\Omega\). For example, define
\[
 \mathcal A_k(Z)=\sum_{n=0}^{N-1}
       (1+2p-k)\mathcal G_p(n-Nk)E_n(Z),\qquad
 \mathcal P(t;Z)=\sum_{n=0}^{N-1}F_n(t)E_n(Z).
 \tag{26}
\]
Equation (12) gives the exact polynomial and operator identities
\[
 f_{N,2p}(Z)=\kappa^{-p}\left[
       \sum_{k\in I_p}(-1)^k\mathcal A_k(Z)
       -2|p|\int_{L_\sigma}
                   \frac{\mathcal P(t;Z)}{1+e^{2\pi iNt}}\,dt
                              \right],
 \tag{27}
\]
\[
 \boxed{
 R^{2p}=\kappa^p\left[
       \sum_{k\in I_p}(-1)^k\mathcal A_k(\Omega)
       -2|p|\int_{L_\sigma}
                   \frac{\mathcal P(t;\Omega)}{1+e^{2\pi iNt}}\,dt
                              \right].}
 \tag{28}
\]
The integrals are absolutely convergent coefficientwise in a
finite-dimensional space. Every original linear turn, prescribed
pivotal cut, or exterior linear contraction may therefore be
applied to (28). Several slots may be replaced in their original
order; at fixed \(N\) the resulting finite tensor integrals are
absolutely convergent. This does not commute neighboring Casimirs
or alter the closing functional.

The original circle conversion remains
\[
 \beta_j=(-1)^j(a_j-a_{j+2}),\qquad
               a_N=a_{N+1}=0
 \tag{29}
\]
as finite endpoint coefficients. Neither \(\mathfrak a(N)\) nor
\(\mathfrak a(N+1)\) is to be substituted for these prescribed
zeros. The entire interpolation in (3) and its original circle
difference may be used with the separate endpoint factors proved
in the coherent source note; (8) changes none of those conventions.
In particular (28) retains the odd simple node and all even-level
normal conditions by the original full-Hermite identification,
not by a value-only spectral replacement.

For \(p=0\) use the separate exact operator \(R^0=I\); on the
physical range \(H_n=\delta_{n0}\), \(D_n=0\). The singular-looking
expressions containing \(1/p\) are not used in that case.

## 5. An absolute compact-color envelope and its limits

The contour has a simple uniform estimate. For \(z=Nw\), (13)--(14)
and a real Gaussian integration give
\[
 \boxed{
 |\mathcal M_p(Nw)|
 \le \frac{C_*}{\sqrt{2|p|N}}\,
  \exp\left\{
     \frac{\pi N}{2|p|}
          [\operatorname{Im}(e_\sigma(p+w))]^2
       \right\}.}
 \tag{30}
\]
For each compact \(K\subset\mathbb C\) and fixed derivative order
\(r\), the same estimate for \(\partial_z^r\mathcal M_p(Nw)\)
holds with \(C_*\) replaced by \(C_{p,K,r}\). Indeed differentiation
inserts \((-2\pi it)^r\); after the real Gaussian is centered, its
center stays bounded on \(K\), and its moments are uniformly
bounded for \(N\ge2\). Differentiation with respect to \(w\), rather
than \(z\), costs the additional factor \(N^r\).

The explicit Gaussian functions in (7) obey the analogous compact
exponential estimate. Hence, for some finite \(B_{p,K}\) independent
of \(N\),
\[
 \sup_{w\in K}\left(
   |\partial_z^rH(Nw)|
   +N^{-1}|\partial_z^rD(Nw)|
   +|\partial_z^r\mathfrak a(Nw)|
                    \right)
       \le C_{p,K,r}N^{-1/2}e^{NB_{p,K}}.
 \tag{31}
\]
This follows directly from (8)--(9), including the factors
\(r(z)\) and \(1-r(z)\); it is not an estimate obtained by
discarding them. The Gaussian tails in the proof are also uniform
on such compact sets.

The envelope (30) need not equal the geometric action. At \(w=0\)
its exponent is already \(\pi|p|N/4\), despite the possible
cancellations in the original finite data. Equations (8), (24),
and (28) supply an exact complex-color source representation and
its contour residues. They do not prove a nonzero exterior
pairing, a geometric contour deformation, or a volume limit.

## Direct source versions

Both complete sources were read as written mathematics. No
mathematical program, test, numerical evaluation, or build was used.

- research_full_hermite_gauss_reciprocity.md:
  ccd241bfcd15e9855ea9aaa10e65c84697874c36149d894edf3ff8dfa2300ee1.
- actual_coherent_filling_gaussian_chirp.md:
  d72f50bf1e9af5b15da89784c198a3cb5060b9ee9c3e6cc04b901049be516522.
