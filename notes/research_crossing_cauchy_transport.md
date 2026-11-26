# Forced finite transport for the original crossing interface

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The one-crossing interface has an exact inhomogeneous first-order
transport law. Its endpoint forcing and full-period condition determine
the finite source. A moving-pole contribution has an explicit nonzero
packet on a separated domain, but the entire kernel need not be that
contribution. This distinction is essential in the proposed
three-to-four attachment.

## 1. The finite recurrence and its endpoint forcing

Use the original matrices, cardinal functions and notation of
[the interface calculation](research_three_four_source_interface.md):
\[
 r=Q^{-1},\quad X=e^{2\pi ix},\quad Y=e^{2\pi iy},\quad
 c_x=N^{-1}e^{-\pi i(N-1)x}(1-X^N),\quad
 C_N(x,y)=h(x)^TMh(y)=\kappa c_xc_yG_N(X,Y).
 \tag{1}
\]
Here the symbol \(G_N(X,Y)\) is the rational Cauchy sum below,
not the sine-factorial interpolant used in Section 3. Put
\[
 b_i(Y)=\frac{Y^i(r;r)_i}{(Y;r)_{i+1}},\qquad
 G_N(X,Y)=\sum_{i=0}^{N-1}\frac{b_i(Y)}{1-Xr^i}.
 \tag{2}
\]
These identities initially hold away from their displayed denominators.

**Proposition 1.** The exact original interface satisfies
\[
 \begin{split}
 (X-Y)G_N(X,Y)+Y(1-X)G_N(rX,Y)&=\frac X{1-X},\\
 (X-Y)C_N(x,y)-qY(1-X)C_N(x-1/N,y)
                                      &=\kappa Xc_yh_0(x).
 \end{split}
 \tag{3}
\]
The second identity is an identity of entire functions of the two
marked angles, including the original even-level antiperiodicity.
In particular,
\[
             C_N(y-1/N,y)=-\kappa q^{-1}h_0(y)^2.
 \tag{4}
\]

*Proof.* Read indices of \(b_i\) cyclically. Its literal ratio and
the initial value give
\[
 (1-Yr^i)b_i-Y(1-r^i)b_{i-1}=\mathbf1_{\{i=0\}}.
 \tag{5}
\]
At \(i=0\), the cyclic predecessor is killed by \(1-r^0=0\),
and \((1-Y)b_0=1\). Multiply (5) by \((1-Xr^i)^{-1}\)
and sum. Use
\[
 \frac{1-Yz}{1-Xz}=\frac{1-Y/X}{1-Xz}+Y/X,
\]
and the corresponding identity for the shifted second sum. The terms proportional to
\(\sum b_i\) cancel, giving the first line of (3).
Since \(c_{x-1/N}=-q^{-1}c_x\) and
\(c_x/(1-X)=h_0(x)\), it gives the second line. The apparent
poles are removable in the original finite matrix expression, so
the identity extends everywhere. Setting \(X=Y\), canceling on
the open nonsingular set and continuing proves (4). \(\square\)

For any actual half-band source \(F_N\), the same identity may be
integrated before taking asymptotics. Horizontal translation of a
complete period gives exactly
\[
 \begin{split}
 &N\int\!\big[(X-Y)F_N(x)
       -qY(1-QX)F_N(x+1/N)\big]C_N(x,y)\,dx\\
 &\hspace{25mm}=\kappa c_yN\int XF_N(x)h_0(x)\,dx.
 \end{split}
 \tag{6}
\]
Both products are periodic: the two half-band signs cancel. No
endpoint or normal is discarded. This is a source-level difference
identity; it does not replace the original bilinear integral by a
Hermitian observation.

## 2. The full-period forced solution

Write \(X_j=Xr^j\), and set
\[
 a_j=\frac{Y-X_j}{Y(1-X_j)},\qquad
 f_j=\frac{X_j}{Y(1-X_j)^2}.
 \tag{7}
\]
Equation (3) says \(G_N(X_{j+1},Y)=a_jG_N(X_j,Y)+f_j\).
Its exact monodromy is
\[
 P:=\prod_{j=0}^{N-1}a_j
       =\frac{Y^N-X^N}{Y^N(1-X^N)},\qquad
 1-P=\frac{X^N(1-Y^N)}{Y^N(1-X^N)}.
 \tag{8}
\]
For \(X,Y\ne0\), \(X^N,Y^N\ne1\), the cyclic forced
solution is therefore uniquely determined:
\[
 \boxed{\quad
 G_N(X,Y)=\frac1{1-P}
    \sum_{j=0}^{N-1} f_j\prod_{k=j+1}^{N-1}a_k .\quad}
 \tag{9}
\]
The empty product is one. This follows by iterating the recurrence
once around the full cycle and using \(X_N=X\); no inverse of an
individual \(a_j\) is required. In particular it remains valid
when \(X=Y\).

More generally, let \(\sigma\) be a field automorphism with
\(\sigma^N=1\), and consider \(\sigma g=ag+b\).
If \(A=\prod_{j=0}^{N-1}\sigma^j(a)\ne1\), its unique field
solution is
\[
 g=\frac{\displaystyle\sum_{j=0}^{N-1}\sigma^j(b)
                      \prod_{k=j+1}^{N-1}\sigma^k(a)}{1-A}.
 \tag{9a}
\]
Iteration proves necessity; applying \(\sigma\) to the numerator
gives \(a\) times that numerator plus \((1-A)b\), proving
sufficiency. This is an exact forced cyclic difference equation,
with no unspecified solution or homogeneous summand. Formula (9)
is its specialization to \(\sigma X=rX\).

Invertibility is not a growth estimate. On compact regions with
\(0<|X|,|Y|<1\),
\[
 |1-P|=\left|\frac XY\right|^N
          \left|\frac{1-Y^N}{1-X^N}\right|.
 \tag{9b}
\]
It can be exponentially small when \(|X|<|Y|\). The exact
normalizing factors and cancellations in the Green numerator must
remain when estimating the original interface.

For the unnormalized interface, the recurrence coefficients are
\(\alpha_j=(X_j-Y)/(qY(1-X_j))\). With
\(\eta=(-1)^{N-1}\), their product and the quasiperiodic closing
denominator are
\[
 \prod\alpha_j=-\eta\frac{X^N-Y^N}{Y^N(1-X^N)},\qquad
 \eta-\prod\alpha_j
       =\eta\frac{X^N(1-Y^N)}{Y^N(1-X^N)}.
 \tag{10}
\]
Thus (9) incorporates exactly \(C_N(x-1,y)=\eta C_N(x,y)\).
Deleting the forcing in (3) would give zero as the only cyclic
solution on this domain. A formal homogeneous phase does not by
itself encode the original finite period.

## 3. Exact contour crossing and its residue packet

Let \(\mathcal G_N(z)\) be the exact sine-factorial interpolant
from [the factorial proof](exact_factorial_interpolation_and_complex_contours.md),
and \(\mathcal P_N(s,Y)\) the exact denominator interpolation from
[the root-product proof](research_root_pochhammer_interpolation.md).
Choose the marked logarithm \(\Log Y=2\pi iy\). Define
\[
 \mathcal A_N(s;Y)=
 \frac{e^{Ns\Log Y+i\pi N(s-s^2)/2-i\pi s/2}
               \mathcal G_N(Ns)}{\mathcal P_N(s+1/N,Y)}.
 \tag{11}
\]
It equals \(b_i(Y)\) exactly at \(s=i/N\). It is holomorphic
and nonzero when
\[
           -1/N<\Re s<1,\qquad |Y|<1,
                         |Ye^{-2\pi is}|<1.
 \tag{12}
\]
Use the lattice kernel
\[
                  L_N(s)=\frac{2\pi iN}{e^{2\pi iNs}-1}.
 \tag{13}
\]
Every lattice pole has residue one. Take an initial positively
oriented contour \(\Gamma_0\) inside (12), enclosing precisely
\(0,1/N,\ldots,(N-1)/N\), and excluding all moving poles
\(s=x+\mathbb Z\). For example a thin rectangle with sides
\(\Re s=-1/(2N),1-1/(2N)\) works when \(x\) is separated
from its real side and \(\Im x\ne0\).
Then the complete original finite sum is exactly
\[
 C_N(x,y)=\frac{\kappa c_xc_y}{2\pi i}
  \int_{\Gamma_0}
   \frac{L_N(s)\mathcal A_N(s;Y)}{1-Xe^{-2\pi is}}\,ds.
 \tag{14}
\]

**Proposition 2.** Suppose \(\Gamma_0\) is enlarged within
(12) to \(\Gamma_1\), crossing exactly the simple moving pole
\(s=x\) and no other pole. Then
\[
 \begin{split}
 C_N(x,y)&=\frac{\kappa c_xc_y}{2\pi i}
  \int_{\Gamma_1}
   \frac{L_N(s)\mathcal A_N(s;Y)}{1-Xe^{-2\pi is}}\,ds
                  +\mathcal R_N(x,y),\\
 \mathcal R_N(x,y)&=
  \frac\kappa N e^{-\pi i(N-1)(x+y)}(1-Y^N)
                                  \mathcal A_N(x;Y).
 \end{split}
 \tag{15}
\]

*Proof.* The derivative of \(1-Xe^{-2\pi is}\) at \(s=x\)
is \(2\pi i\). Thus the residue of the integrand is
\(L_N(x)\mathcal A_N(x;Y)/(2\pi i)\). Enlargement adds
that residue to the contour divided by \(2\pi i\). Subtracting
it from the enlarged contour gives the original sum. Since
\(L_N(x)/(2\pi i)=N/(X^N-1)\), its negative contribution,
after multiplication by \(\kappa c_xc_y\), is exactly the
second line of (15). In particular the factor \(1-X^N\)
cancels exactly, not asymptotically. \(\square\)

On every marked compact domain with
\(0<\Re x<1\), \(|Y|<1\), and \(|Y/X|<1\), this one
residue has a nonzero holomorphic expansion. Write
\(\mathcal J(x)=\int_0^x\Log(2\sin\pi t)\,dt\), on the
marked sine-factorial branch, and
\(I_Y(x)=[\operatorname{Li}_2(Y/X)-\operatorname{Li}_2(Y)]/(2\pi i)\),
using the disk dilogarithms. Then
\[
 \begin{split}
 \mathcal R_N(x,y)
   &=\kappa N^{-1/2}a_C(x,y)e^{N\chi(x,y)}(1+O(N^{-1})),\\
 \chi(x,y)&=\mathcal J(x)+\frac{i\pi}{2}(x-x^2)
                 +x\Log Y-I_Y(x)-\pi i(x+y),\\
 a_C(x,y)&=
 \frac{e^{\pi i(x/2+y)}\sqrt{2\sin\pi x}}
                 {\sqrt{(1-Y)(1-Y/X)}}.
 \end{split}
 \tag{16}
\]
The logarithms and roots are exactly those in (11); their branches
are not reset. The two quoted interpolation theorems prove the
expansion, with all fixed derivatives. In particular its derivative
equations are
\[
       e^{\chi_x}=\frac{Y(1-X)}{X-Y},\qquad
       e^{\chi_y}=\frac{Y-X}{1-Y}.
 \tag{17}
\]
The first is precisely the leading homogeneous relation in (3).
At \(X=Y\), the denominator interpolation in (11) reaches its
endpoint boundary \(Y/X=1\); (16) is not a holomorphic packet
across that diagonal. The exact kernel stays entire by (1).
Equation (4) supplies a particularly simple exact layer adjacent to
the diagonal. Neither (15) nor (16) proves that its remaining contour
is smaller than the residue. All contour sides and their original
factorial endpoints remain in the first term of (15).

## 4. What the residue would require in the three-to-four convolution

There is a precise domain issue even at the alternating reference
from [the interface note](research_three_four_source_interface.md).
Write its exterior parameter as \(K=e^{2\pi ix_{34}}\), and
write \(Z=e^{2\pi iz}\) for the intermediate wire in
\(N\int V_3(x,z)C_N(z,y)\,dz\). On an original regular
three-vertex critical chart its selected index equations are
\[
 U(1-V)=K^{-1}-1,\qquad V(1-U)=Z^{-1}-1,
 \qquad e^{\Phi_{3,z}}=\frac{ZV-1}{V(1-Z)}.
 \tag{18}
\]
If the residue phase (16) supplied this crossing step with
\(x=y=x_{34}\), stationarity in \(z\) would require
\[
                 V=\frac K{Z(K-1)+K}.
 \tag{19}
\]
Substituting in (18), without resetting any logarithms, gives the
necessary algebraic equation
\[
 \frac{Z(K-1)(KZ+2K-Z)}{K(KZ+K-Z)}=0.
 \tag{20}
\]
On the regular nonzero domain it forces
\[
 Z=\frac{2K}{1-K},\qquad
 - .281<\Re Z<-.280,\quad 1.274<\Im Z<1.275,\quad |Z|>1.30,
 \tag{21}
\]
and the marked intermediate angle has
\(.284<\Re z<.285\), \(-.043<\Im z<-.042\).
These bounds are outward consequences of the validated quartic root.
Although \(|K/Z|<.468\) lies safely inside the residue domain,
\(|Z|>1\) lies outside the denominator domain of the proved
three-vertex packet. Thus this proposed factorization cannot keep
both of its factors in the existing \(|X|,|Y|<1\) packet charts.
Equation (20) is only a necessary algebraic condition; it does not
claim an actual contributing stationary point on an unproved branch.
The full forced transport (3)--(9), or a continuation retaining the
new denominator crossings, is needed to resolve that issue.

## 5. The actual corner under a crossing insertion

The crossing does not invalidate every existing estimate. Let
\(L=\lfloor\epsilon N\rfloor\),
\(E_L=M^TP_LJM P_LM\) be the actual square corner, and
\[
        D_L=\kappa^{-1}ME_LM^{-1}
             =JM^{-1}P_LJM P_L=D_LP_L.
 \tag{22}
\]
For every fixed integer \(r\),
\[
 \boxed{\quad
 \|M(E_LM^r)M^{-1}\|
  \le\sqrt{L+1}(1+|r|)^L\|ME_LM^{-1}\|
  \le\operatorname{poly}(N)
       e^{N[\sigma_\epsilon+\epsilon\log(1+|r|)]},
 \quad\sigma_\epsilon=\epsilon\log(2e/\epsilon).\quad}
 \tag{23}
\]
Indeed the original sine-binomial entries obey
\(|M_{jk}|\le{j\choose k}\) for \(k\le j<N\): apply
the decrease of \(\sin t/t\) to each factor of
\(S_j/(S_kS_{j-k})\). If \(B_{jk}={j\choose k}\), the
exact Pascal convolution gives
\((B^r)_{jk}=r^{j-k}{j\choose k}\) for nonnegative integers
\(r\). Since \(M^{-1}=\overline M\), the entrywise bound
also holds with \(|r|\) for negative powers. Every row of the
first \(L+1\) square therefore has sum at most
\((1+|r|)^L\); its Frobenius norm is at most
\(\sqrt{L+1}(1+|r|)^L\). Lower triangularity and (22) give
\(D_LM^r=D_L(P_LM^rP_L)\). The
[original corner bound](research_three_chain_fourier_corner_transfer.md#4-a-larger-deleted-corner-for-a-larger-source-domain)
then proves (23).

For \(\epsilon=1/40\) and \(|r|\le3\), the extra cost is
less than \(\log4/40<7/200\). This is smaller than the
previous homogeneous complete-ended reserve \(31/600\), leaving
more than \(1/60\) at the level of this one-factor budget.
It does not bound the other factors of a mixed word, identify its
action, or prove that every corner in such a word is negligible.

## 6. A global endpoint criterion for the actual interface

There is also a useful regime in which the exact forced solution has
an endpoint expansion. This concerns the full interface, not only its
moving-pole contribution. For \(0<|Y|<1\), put
\[
 F_Y(s)=\mathcal J(s)+s\log|Y|-\Re I_Y(s),\quad 0\le s\le1,
 \qquad d=1-|Y|^2,\quad v=Y-|Y|^2.
 \tag{24}
\]
Here the functions on the real interval have the branches already
specified above. In particular \(F_Y(0)=0\) and
\(F_Y(1)=\log|Y|<0\). Define an open region \(\mathcal E\)
as follows. If \(2|v|\le d\), include \(Y\) in
\(\mathcal E\). Otherwise, choose \(\theta_0=\arg v\) in
\((0,2\pi)\), set
\[
 \alpha=\arccos\frac d{2|v|},\qquad
 s_+(Y)=\frac{\theta_0+\alpha}{2\pi},
 \tag{25}
\]
and include \(Y\) precisely when \(F_Y(s_+(Y))<0\).
The first alternative includes every positive real \(Y<1\).

**Theorem 3.** Let \(\mathcal K\) be a compact subset of
\(\mathcal E\), and let \(\mathcal X\) be a compact subset
of \(\{X:|X|\ne1\}\). Uniformly for \(Y\in\mathcal K\)
and \(X\in\mathcal X\), for every fixed integer \(p\ge1\),
\[
 G_N(X,Y)=\sum_{i=0}^{p-1}\frac{b_i(Y)}{1-Xr^i}
                                  +O_{\mathcal K,\mathcal X,p}(N^{-p}).
 \tag{26}
\]
The same assertion holds with every fixed derivative on smaller
compact neighborhoods. Consequently the actual marked kernel is
nonzero for all sufficiently large \(N\) and has the packet
\[
 C_N(x,y)=\kappa h_0(x)h_0(y)\{1+O(N^{-1})\}.
 \tag{27}
\]
The finite sum in (26), after multiplication by
\(\kappa c_xc_y\), is exactly
\(h(x)^TP_{p-1}Mh(y)\), with no change of normalization.

For a fixed \(0<\epsilon<1\), let
\(L_N=\lceil\epsilon N\rceil-1\), and put
\(\eta_{\mathcal K,\epsilon}
 =-\max_{Y\in\mathcal K,\,\epsilon\le s\le1}F_Y(s)>0\).
There is the stronger exact-row tail estimate
\[
 \left|h(x)^T(1-P_{L_N})Mh(y)\right|
 \le |c_xc_y|\operatorname{poly}(N)
                          e^{-N\eta_{\mathcal K,\epsilon}}.
 \tag{28}
\]
Thus (28) controls the whole input Fourier period at any fixed
nonzero height, of either sign. It is not a bound on an
arbitrary subsequent bilinear contraction.

*Proof.* The sign of \(F_Y'(s)\), for \(0<s<1\), is
the sign of
\[
 \begin{split}
 D_Y(s)&=|Y(1-e^{-2\pi is})|^2
                   -|1-Ye^{-2\pi is}|^2\\
 &=-d+2(\Re Y-|Y|^2)\cos(2\pi s)
                              +2\Im Y\sin(2\pi s).
 \end{split}
 \tag{29}
\]
At both endpoints this sinusoid is \(-|1-Y|^2<0\).
If \(2|v|\le d\), the profile is strictly decreasing apart
from at most one stationary point. Otherwise \(D_Y>0\) on
exactly one interval lying strictly inside \((0,1)\): since
\(D_Y(0)<0\), the choices in (25) satisfy
\(0<\theta_0-\alpha<\theta_0+\alpha<2\pi\).
The profile first decreases, then increases, then decreases. Its
only possible competing maximum is \(s_+(Y)\). The stated
criterion therefore says exactly that
\(F_Y(s)<0\) for every \(0<s\le1\).

This condition is open. Indeed, near zero the derivative is
\(\log s+O(1)\), uniformly when \(Y\) ranges over a compact
subset of \(0<|Y|<1\). On any remaining closed subinterval,
strict negativity persists by continuity. This also proves the
positive minimum \(\eta_{\mathcal K,\epsilon}\).

The uniform sine-factorial endpoint estimate and the smooth
denominator Riemann sum give, for all \(0\le i<N\),
\[
             \log|b_i(Y)|=NF_Y(i/N)+O_{\mathcal K}(\log N).
 \tag{30}
\]
For clarity, the factorial estimate follows by subtracting
\(\log s+\log(1-s)\) from \(\log(2\sin\pi s)\),
applying elementary factorial bounds to those two singular terms,
and the ordinary Riemann estimate to the smooth remainder.
The denominator logarithm is uniformly smooth because
\(|Y|\le\rho<1\). Since
\(|1-Xr^i|\ge\big||X|-1\big|\), uniformly bounded below on
\(\mathcal X\), (30)
proves (28) and bounds every fixed lower-index complement
\(i\ge\delta N\) exponentially.

Choose a fixed \(\delta>0\) so small that
\(2\pi\delta\rho/(1-\rho)<1\). For \(p\le i\le\delta N\),
the literal finite coefficients satisfy
\[
 |b_i(Y)|\le\frac1{1-\rho}
           \left(\frac\rho{1-\rho}\right)^i S_i,
 \qquad
 S_i\le\left(\frac{2\pi}{N}\right)^p p!
                              (2\pi\delta)^{i-p}.
 \tag{31}
\]
Summing the resulting geometric series gives \(O(N^{-p})\).
Together with the exponentially bounded complement, this proves
(26). Its first term is \(1/[(1-X)(1-Y)]\); it is bounded
away from zero on the stated compact set. The nonzero factors
\(c_x,c_y\) and their exact identification with \(h_0\) give
(27). Holomorphy and Cauchy's formula on slightly larger compact
sets prove the derivative assertions. \(\square\)

The validated alternating reference belongs to this open region:
the focused checker proves, by outward evaluation of (24)--(25),
\[
 .441<s_+(K)<.442,\qquad F_K(s_+(K))<-\frac{69}{1000},
 \qquad F_K(1/40)<-\frac{8}{100},
 \qquad K=e^{2\pi ix_{34}}.
 \tag{32}
\]
Since the profile has no other possible maximum, the full tail in
(28) above the \(1/40\) row cutoff has a uniform exponent less
than \(-69/1000\) on a sufficiently small fixed neighborhood of
\(K\). Formula (27) is an actual interface asymptotic there,
uniformly over the whole input period at a fixed nonzero height.
This leading term is rank one; it is not the geometric mixed
vertex phase. In the exact three-to-four convolution its finite
prefix becomes \(h(x)^TA_3P_{p-1}Mh(y)\). Formula (26) with
fixed \(p\) gives only polynomial relative suppression before
that contraction. Formula (28) gives an exponential tail but retains
an increasing-rank prefix. Neither permits discarding the prefix
or transferring its error through the original signed contraction
without a corresponding source estimate.

In particular this conclusion also applies to the exterior
intermediate parameter \(Z_0=2K/(1-K)\) in (21), with its
actual \(c_z\) from (1). Here \(z=\Log Z_0/(2\pi i)\).
On the lower half of the factorial strip one can write the bulk
phase entirely with disk dilogarithms:
\[
 f(z;K)=\frac{\operatorname{Li}_2(Z_0^{-1})-\pi^2/6
                  -\operatorname{Li}_2(K/Z_0)
                  +\operatorname{Li}_2(K)}{2\pi i}
                               +z\Log K.
 \tag{33}
\]
This follows by differentiating the original sine-factorial
primitive and matching its value at zero; no new logarithmic lift
is introduced. The focused outward check proves
\[
                   \Re\{f(z;K)-\Log Z_0\}<-\frac{31}{100}.
 \tag{34}
\]
Indeed the exact quotient of the moving residue (15) and the
endpoint term is
\[
 \frac{\mathcal R_N(z,y)}{\kappa h_0(z)h_0(y)}
   =\frac{N(1-Z_0)(1-K)}{1-Z_0^N}\,
                                      \mathcal A_N(z;K).
 \tag{35}
\]
The quoted interpolation expansion and (34) make (35)
\(O(\operatorname{poly}(N)e^{-31N/100})\), uniformly on a
small fixed neighborhood. Consequently the remaining contour in
(15) retains the same leading endpoint packet (27); it cannot
be bounded below the residue before the two kernels are combined.
This does not exclude the exterior three-variable stationary
contribution. It identifies a specific cancellation that any proof
selecting it from the full source must preserve.

Run `python3 experiments/check_crossing_cauchy_transport.py`.
The [record](../repro/results/research-crossing-cauchy-transport.json)
separates exact finite identities, scalar bounds and the inherited
geometric enclosure from the unproved complementary-contour problem.
