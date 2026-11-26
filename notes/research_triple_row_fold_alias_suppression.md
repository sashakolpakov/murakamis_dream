# The complete finite fold-row contribution has a strict charged gap

Private written proof, 17 November 2026.

The positive triple-row pressure is largest at the closing fold.
Nevertheless the complete original trace over a sufficiently small
fixed fold window has a strictly smaller exponential rate. The value
and first-normal terms must be kept together to obtain this estimate.
The proof compares their actual finite sum with one scalar saddle
polynomial and then uses the original unit-charge trace kernel.

The two incoming physical rows are values, with their centered degrees
in a fixed bulk compact set. The closing power is any fixed signed
integer, including zero. Every nonfold row remains untouched. This is
neither an estimate of the entire signed scalar nor a volume theorem.

## 1. Original source, centered rows, and the fold packet

Use
\[
 N\ge2,\qquad D=N-1,\qquad q=e^{\pi i/N},\qquad
 \eta=(-1)^D,\qquad \kappa=q^{D^2/2},
\]
\[
 P_N(Z)=2T_N(Z/2)+2,\qquad
 \phi_N(f)=\eta N^2[Z^D]\operatorname{rem}_{P_N}f,
 \qquad \mathcal A_N=\mathbb C[Z]/(P_N).
 \tag{1}
\]
All fractional powers use the displayed logarithm of \(q\).
The original Newton basis, turn, and physical rows are
\[
 e_r(Z)=S_r^{-2}\prod_{a<r}(c_a-Z),\qquad
 S_r=\prod_{a=1}^r2\sin(\pi a/N),\qquad S_0=1,\qquad Te_r=e_{D-r},
\]
\[
 c_j=2\cos((2j+1)\pi/N),\qquad
 F_j(Z)=K_N(c_j,Z),\qquad
 K_N(w,Z)=\sum_{r=0}^D e_r(w)e_r(Z).
 \tag{2}
\]
At a double node set \(G_\ell(Z)=\partial_wK_N(c_\ell,Z)\).
There is no prescribed \(G\) row at the odd simple node.
Let
\[
 X_j=(j+1/2)/N,\qquad t_j=\pi-2\pi X_j,
 \qquad H_{jk,N}=T(F_jF_k).
 \tag{3}
\]
The product in (3) is the original full product, and \(H_{jk,N}\)
means its canonical representative. In particular
\[
 H_{jk,N}(c_\ell)=\Gamma_{jk\ell}
       =\phi_N(F_jF_kF_\ell),\qquad
 H_{jk,N}'(c_\ell)=\phi_N(F_jF_kG_\ell)
 \tag{4}
\]
at every double node. The second identity is an original spectral
first normal, not differentiation of a continuous row label.

Fix a compact set
\[
 \mathcal K\Subset
 \{(x,y):0<x,y<1/2,\ x+y>1/2\}.
 \tag{5}
\]
Throughout the theorem \((X_j,X_k)\in\mathcal K\).
Write \(\mathcal G\) for the positive triple-row pressure in the
calibration source, and put
\[
 M(x,y)=\mathcal G(x,y,1/2),\qquad
 \mathcal F_{x,y}(t)
       =\mathcal G(x,y,1/2-t/(2\pi)).
 \tag{6}
\]
Here (6) is the holomorphic extension selected by the strict interior
saddle, on a sufficiently small neighborhood of the fold. It is real
and even in real \(t\), and
\[
 \mathcal F_{x,y}(0)=M(x,y),\qquad
 \mathcal F_{x,y}'(0)=0,\qquad
 \mathcal F_{x,y}''(0)<0.
 \tag{7}
\]
These statements hold uniformly on \(\mathcal K\). In particular there
are fixed \(T_0,H_0,c,C>0\) such that
\[
 \Re\mathcal F_{x,y}(s+ih)
       \le M(x,y)-cs^2+Ch^2
       \quad(|s|\le T_0,\ |h|\le H_0).
 \tag{8}
\]
For example, first use the strict real quadratic maximum, then Taylor
expand in the imaginary direction. The first derivative on the real
axis is real, so its contribution to the real part is zero; a uniform
second derivative bound gives the last term in (8).

We use the actual fold calibration in the following precise form.
On each of finitely many parameter neighborhoods covering
\(\mathcal K\), there is one polynomial \(W_{jk,N}(Z)\), obtained by
retaining a fixed interior saddle window of the original positive
Newton sum. After decreasing \(T_0,H_0\), there are constants
\(B,C_0,\kappa_0>0\), common to this finite cover, with
\[
 |W_{jk,N}(-2\cos t)|
       \le C_0N^B e^{N\Re\mathcal F_{X_j,X_k}(t)}
       \quad(|\Re t|\le T_0,\ |\Im t|\le H_0),
 \tag{9}
\]
and at every physical double row with \(0<t_\ell<T_0\),
\[
 \begin{split}
 |H_{jk,N}(c_\ell)-W_{jk,N}(c_\ell)|
 &\le C_0N^B e^{N(M(X_j,X_k)-\kappa_0)},\\
 |H_{jk,N}'(c_\ell)-W_{jk,N}'(c_\ell)|
 &\le C_0N^B e^{N(M(X_j,X_k)-\kappa_0)}.
 \end{split}
 \tag{10}
\]
At the odd simple row, only the value estimate is used.

These are established properties of this specified source, rather
than assumptions on arbitrary arrays. In particular the window is
an ordinary polynomial: its third-row factor is exactly
\(e_m(2\cos2\pi X)\), with the original half-step retained in
the factorial arguments. The high derivative band
\(\ell<m\le D-\ell\) approaches the excluded face \(m/N=1/2\)
as the closing row approaches the fold. The strict boundary gap in
the calibration controls that band, as well as the omitted low terms.
An inserted \(G_j\) or \(G_k\) at one of the two bulk incoming
boundaries is not covered by (10).

## 2. The literal finite fold trace

The distinct double rows are
\(\mathcal D_N=\{0,\ldots,\lfloor N/2\rfloor-1\}\).
At odd \(N\) there is also the simple row \(c_*=-2\).
For a canonical polynomial \(f\), the exact residue form of (1) is
\[
 \phi_N(f)=
 \eta\sum_{\ell\in\mathcal D_N}
       \{(4-c_\ell^2)f'(c_\ell)-c_\ell f(c_\ell)\}
       +\mathbf1_{N\ \mathrm{odd}}f(-2).
 \tag{11}
\]
Indeed \(\phi_N(f)=\eta N^2\sum_{P_N(c)=0}
\operatorname{Res}_{Z=c}f(Z)/P_N(Z)\). The double-root Taylor
coefficients from the confluent source give
\[
 \frac1{P_N(Z)}=
 \frac{4-c^2}{N^2(Z-c)^2}-\frac{c}{N^2(Z-c)}+O(1),
 \tag{12}
\]
and at the odd simple node \(P_N'(-2)=N^2\).

Fix an integer \(p\), independent of \(N\). Let \(R\) be the
original crossing, and for a positive cutoff \(T_N\) define the
actual partial trace
\[
 \begin{split}
 Z^{\rm fold}_{N,p}(j,k;T_N)
 ={}&\eta\!\sum_{\substack{\ell\in\mathcal D_N\\0<t_\ell<T_N}}
 \bigl\{(4-c_\ell^2)(R^pH_{jk,N})'(c_\ell)
                    -c_\ell(R^pH_{jk,N})(c_\ell)\bigr\}\\
 &+\mathbf1_{N\ \mathrm{odd}}(R^pH_{jk,N})(-2).
 \end{split}
 \tag{13}
\]
All multiplication and derivatives here are those of the original
full algebra. Canonical multiplication preserves every displayed jet.
Equation (11) splits the full scalar exactly into (13) and the
remaining double-row sum. No estimate of that remaining sum is made.

The exact crossing representative on this angular chart is
\[
 \rho_{N,p}(t)=q^{pD^2/4}\exp\!\left(\frac{ipNt^2}{4\pi}\right).
 \tag{14}
\]
The unit scalar \(q^{pD^2/4}=\kappa^{p/2}\) is retained.
To verify the value and first-normal assertion, use
\[
 R(c_\ell)=\kappa(-1)^\ell q^{\ell(\ell+1)},\qquad
 \frac{R'(c_\ell)}{R(c_\ell)}
       =\frac{i(D-2\ell)}{4\sin((2\ell+1)\pi/N)}.
 \tag{15}
\]
Substitution of \(Nt_\ell=\pi(D-2\ell)\) proves equality
of the values in (14); their exponents differ only by an integral
multiple of \(2\pi i\). Moreover
\[
 \frac{\partial_t\rho_{N,p}}{2\sin t\,\rho_{N,p}}
       =\frac{ipNt}{4\pi\sin t}
 \tag{16}
\]
is precisely the required spectral logarithmic derivative at every
double row. At \(t=0\), only the value is prescribed.
This does not identify (14) with the canonical crossing off grid.

For an even holomorphic scalar \(A(t)\) on a rectangle containing
the selected rows, put \(g(t)=\sin t\,A(t)\). For \(t_\ell>0\),
\[
 (4-c_\ell^2)f'(c_\ell)-c_\ell f(c_\ell)
                   =2g'(t_\ell),
 \tag{17}
\]
whenever \(A(t)=f(-2\cos t)\) to the required jets.
The reflected row has the same derivative of the odd function \(g\).
Since
\[
 P_N(-2\cos t)=2-2\eta\cos Nt
              =N^2(t-t_\ell)^2+O((t-t_\ell)^4),
 \tag{18}
\]
the residue of \(g/P_N\) at each angular row is
\(g'(t_\ell)/N^2\). At an odd center, \(g(0)=0\) and
that residue is \(A(0)/N^2\). Thus the exact symmetric
angular-window trace is
\[
 \boxed{\quad
 \mathcal L_{N,T_N}(A)=
     \frac{\eta N^2}{2\pi i}
       \oint_{\partial\mathcal R_N}
          \frac{\sin t\,A(t)}{P_N(-2\cos t)}\,dt,
 \quad}
 \tag{19}
\]
where \(\mathcal R_N=[-T_N,T_N]+i[-H,H]\) has positive
orientation. Both lifts of every double spectral row are included,
and they give exactly (11), not twice that value. The odd center
contributes its one value. No independent normal is invented there.

## 3. Strict suppression of the complete fold window

**Theorem.** For every compact set (5) and fixed integer \(p\),
there are fixed \(T,H,\delta>0\) and constants \(C_1,B_1\)
such that, for every sufficiently large level of either parity and
all physical pairs with \((X_j,X_k)\in\mathcal K\),
\[
 \boxed{\quad
 |Z^{\rm fold}_{N,p}(j,k;T_N)|
       \le C_1N^{B_1}
             e^{N(M(X_j,X_k)-\delta)}.
 \quad}
 \tag{20}
\]
Here \(T_N\) is any nearest positive midpoint cutoff satisfying
\[
       e^{iNT_N}=-\eta,\qquad |T_N-T|\le\pi/N.
 \tag{21}
\]
In particular \(T/2\le T_N\le2T\) for large \(N\).
The windows and the gap are independent of \(j,k,N\) within the
stated scope. No sign restriction on \(p\) is imposed.

**Proof.** Choose \(T,H\) using the uniform constants in
(8)--(10), so that
\[
 2T<T_0,\qquad H<H_0,\qquad
 \frac{|p|\,2T}{2\pi}\le\frac14,\qquad CH\le\frac14.
 \tag{22}
\]
The condition involving \(p\) is void when \(p=0\).
All inequalities may be made strict.

First compare the literal trace (13) with the trace of
\[
          A_{jk,N,p}(t)=\rho_{N,p}(t)W_{jk,N}(-2\cos t).
 \tag{23}
\]
It is a single even holomorphic function. On real physical rows
the crossing values have modulus one. Its spectral first normals
have polynomial size by (15), uniformly through the last double row.
Equations (10)--(11), and the at most \(N\) selected rows, therefore
give
\[
 Z^{\rm fold}_{N,p}(j,k;T_N)
    =\mathcal L_{N,T_N}(A_{jk,N,p})
       +O\!\left(N^{B_2}e^{N(M(X_j,X_k)-\kappa_0)}\right).
 \tag{24}
\]
This comparison uses both actual values and first normals. The odd
simple error uses only its value. There is no interpolation repair
and no discarded exterior trace packet.

At a vertical midpoint side \(s=\pm T_N\), (18) gives exactly
\[
 P_N(-2\cos(s+ih))=2+2\cosh Nh,
 \qquad |P_N(-2\cos(s+ih))|^{-1}\le e^{-N|h|}.
 \tag{25}
\]
On either fixed horizontal side, the factorization
\[
 P_N(-2\cos t)=(1-\eta e^{iNt})(1-\eta e^{-iNt})
\]
gives
\[
             |P_N(-2\cos(s\pm iH))|^{-1}
                         \le C_2e^{-NH}.
 \tag{26}
\]
There is no pole on the rectangle boundary.

The exact crossing has modulus
\[
        |\rho_{N,p}(s+ih)|
                 =\exp\!\left(-\frac{pNsh}{2\pi}\right).
 \tag{27}
\]
Combining (8), (9), and (25)--(27), the exponential part of the
integrand in (19), on all four sides, is at most
\[
 M(X_j,X_k)-cs^2+Ch^2
                +\frac{|p|\,2T}{2\pi}|h|-|h|.
 \tag{28}
\]
By (22), its last three terms are at most \(-|h|/2\).
On the horizontal sides this is at most \(M-H/2\).
On the vertical sides it is at most
\(M-cT_N^2\le M-cT^2/4\), including at \(h=0\).
The remaining prefactors, the sine factor, and the contour lengths
cost only a uniform polynomial in \(N\). Equation (19) consequently
bounds the main term in (24) by
\[
 C_3N^{B_3}
    e^{N(M-\min\{H/2,cT^2/4\})}.
 \tag{29}
\]
Together with (24) this proves (20), for example with
\[
             \delta=\min\{\kappa_0,H/2,cT^2/4\}>0.
 \tag{30}
\]
All constants can be chosen on the finite parameter cover used in
(9)--(10). The nearest-midpoint rule affects none of these strict
inequalities for sufficiently large \(N\). \(\square\)

## 4. Simultaneous folding of the three original boundaries

The same argument also gives a tensor statement without discarding
any mixed first normal. Define the actual three-boundary polynomial
\[
 \mathscr G_N(Z_1,Z_2,Z_3)=
    \phi_U\!\left[\prod_{i=1}^3K_N(Z_i,U)\right].
 \tag{31}
\]
It is canonical in each free variable. Its value at a physical triple
is \(\Gamma_{j_1j_2j_3}\); differentiating in any subset of the
three variables inserts exactly the corresponding \(G\) rows.
The simultaneous-fold part of the calibration supplies one actual
polynomial window \(\mathscr W_N\) approximating all eight such
entries with an exponential gap near \((Z_1,Z_2,Z_3)=(-2,-2,-2)\).
At an odd simple row, only the entries not differentiating that
spectral variable are prescribed or used.

Put
\[
 M_3=\mathcal G(1/2,1/2,1/2),\qquad
 \mathcal F_3(\mathbf t)=
     \mathcal G(1/2-t_1/(2\pi),1/2-t_2/(2\pi),
                                      1/2-t_3/(2\pi)).
 \tag{32}
\]
The calibration gives its separately even holomorphic extension,
with a strictly negative real Hessian at zero. Hence, on a fixed
small product rectangle, uniformly,
\[
 \Re\mathcal F_3(\mathbf s+i\mathbf h)
       \le M_3-c|\mathbf s|^2+C|\mathbf h|^2,
 \qquad
 |\mathscr W_N(-2\cos\mathbf t)|
       \le N^{O(1)}e^{N\Re\mathcal F_3(\mathbf t)}.
 \tag{33}
\]
Its actual mixed-jet error has size
\(N^{O(1)}e^{N(M_3-\kappa_3)}\) for some \(\kappa_3>0\).

**Corollary.** Fix any signed integer vector
\(\mathbf p=(p_1,p_2,p_3)\). Apply the partial spectral trace
in (13) independently to the three boundary variables of
\[
                  \left(\prod_{i=1}^3R(Z_i)^{p_i}\right)
                                     \mathscr G_N(\mathbf Z),
 \tag{34}
\]
using sufficiently small fixed fold windows in every coordinate.
The resulting complete finite tensor sum has modulus at most
\[
                       N^{O(1)}e^{N(M_3-\delta_3)}
 \tag{35}
\]
for a fixed \(\delta_3>0\), at both level parities.

**Proof.** Compare the actual finite tensor trace with
\(\mathscr W_N\) first. The product rule uses exactly the eight
mixed first jets in the calibration, with only polynomial factors
from crossing derivatives, spectral weights, and the number of
rows. Its error is \(N^{O(1)}e^{N(M_3-\kappa_3)}\).
There is no value-only substitution in this comparison.

For the window polynomial the exact integral is the product of
the three oriented contour functionals (19), with multiplier
\[
           \prod_{i=1}^3
             \rho_{N,p_i}(t_i)\sin t_i/P_N(-2\cos t_i).
 \tag{36}
\]
Its prefactor is \((\eta N^2/(2\pi i))^3\); all three crossing
constants in (14) are retained. Choose the widths and heights so
that \(|p_i|\,2T_i/(2\pi)\le1/4\) and \(CH_i\le1/4\).
On every product of boundary sides, (25)--(28) now give the
joint upper action
\[
                 M_3-c\sum_i s_i^2-\frac12\sum_i|h_i|.
 \tag{37}
\]
For each coordinate its contour side is either horizontal, with
\(|h_i|=H_i\), or vertical, with
\(|s_i|=T_{i,N}\ge T_i/2\). Thus all product-side integrals
have a fixed strict gap, at least
\(\sum_i\min\{H_i/2,cT_i^2/4\}\). Adding the mixed-jet
comparison error proves (35). Odd centers have precisely the
single-value multiplicities already proved in (19). \(\square\)

The corollary concerns the finite product of the three fold-row
sets. Every term with at least one boundary row outside those sets
remains in the original tensor trace and is not estimated by (35).
No additional spectator or later boundary normal is inserted into
this statement without its own estimate.

## 5. Meaning of the cancellation and retained scope

For a periodic scalar polynomial \(f(2\cos\vartheta)\), the
full mirrored trace can also be written
\[
 \phi_N(f)=-\eta\sum_{a=0}^{N-1}
    \left.\partial_\vartheta
       \{\sin\vartheta\,f(2\cos\vartheta)\}\right|_
                           {\vartheta=(2a+1)\pi/N}.
 \tag{38}
\]
Its continuous zero Fourier alias is zero. At the odd angular
center the derivative in (38) encodes only the one spectral value.
The exponential \(-|h|\) in (28) is the first nonzero charge of
this original trace, not an assumed oscillation of arbitrary small
arrays. The vertical sides in (19) are retained and paid by their
strict real boundary gap. Their disappearance has not been asserted.

In particular the positive fold maximum of \(\Gamma_{jk\ell}\)
cannot be used as a positive leading term of the crossed closing.
The value and independent spectral-normal entries combine before
the estimate. For calibration, at \(p=0\) the entire scalar is
\[
             \phi_N(H_{jk,N})=(F_jF_k)(c_0)=1,
 \tag{39}
\]
even when its positive physical values have exponential pressure.
The theorem does not require (39) to estimate the fold window.

For \(V_n=\kappa^nTR^{-n}T\), the original observation
\(\phi_N(R^\sigma V_n(F_jF_k))\) satisfies the following identity.
Frobenius adjointness and \(TR^\sigma=R^{-\sigma}\) give
\[
 \phi_N(R^\sigma V_n(F_jF_k))
       =\kappa^n\phi_N(R^{-(n+\sigma)}H_{jk,N}),
                    \qquad \sigma\in\{1,-1\}.
 \tag{40}
\]
Thus (20) applies to its exact fold-row part with
\(p=-(n+\sigma)\), keeping the unit scalar \(\kappa^n\).
All rows outside the selected window in (13), all possible later
normal observations at \(j,k\), and every external source factor
remain outside the estimate. In particular there is no assertion
that a first charged saddle away from the fold contributes, or that
the full scalar is nonzero or has a specified filled-volume rate.

## Complete direct sources

Both complete direct texts were read at the following pins, and every
used implication was checked. The calibration's errors are relative
to the local real pressure; inequality (8) makes them the uniform
fold-ceiling estimates (10) used here.

* [Actual full-normal fold calibration](research_triple_row_fold_full_normal_calibration.md),
  SHA256 d7348d7376a09855b912a5b13d8915f5a1bc23be9dd73ae649cfb849d9701add:
  fixed source polynomial, centered fold phase, and actual closing-row
  value and first-normal errors, including all eight simultaneous
  first-jet entries.
* [Confluent row closing](research_confluent_row_closing_and_positive_quotient.md),
  SHA256 daf5760f74dbd9d9c9646a1a18b95cdffc1f42ebc3cbcfc0a1b9f79b2ad77251:
  original full Frobenius normalization, double-root Taylor data,
  crossing values/normals, and original turn conventions.

Only written mathematics, source-text reads, and metadata hashes were
used. No mathematical programs, numerical tests, builds, or compilations
were run. Adopted notes and public manuscripts are unchanged.
