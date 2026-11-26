# Meridian transport of the entire completion column and its Fourier norms

Private written proof, 19 November 2026.

The physical highest-block completion has an exact change of meridian
frame, coefficient by coefficient through its full cap. That change
and its inverse have polynomial norms on a scaled meridian disk.
Consequently every positive diagonal weighted norm of the entire
column is preserved up to polynomial factors. This includes the
actual circle Fourier norm before and after the factorial output
transform, with all fixed true meridian jets.

The seed changes by its specified conjugation. It is not silently
held fixed. The conclusion concerns whole-column norms, not values
of a coherent kernel or a lower bound for its original closing.
The complete proof directs are H and F, pinned at the end.

## 1. The physical column and its exact moving frame

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and \(Q=q^2\).
Keep this quantum parameter fixed and set \(M=e^\mu\),
\(x=-M/q\). There is one opened head and \(r\ge1\) remaining
heads. Let \(U=V_N^{\otimes r}\), with its original occupation
basis, and let \(E(M),K(M),F(M)\) denote the ordered totals on
\(U\). On an individual head the actual arrows are
\[
 E(M)w_a=(MQ^{-a}-M^{-1})w_{a-1}\quad(a>0),\qquad
 Fw_a=(1-Q^{a+1})w_{a+1},\qquad Kw_a=xQ^{-a}w_a.
 \tag{1}
\]
The two outward arrows are zero. Let \(i_0\) insert the opened
head's \(w_0\), and let \(p_n\) extract its occupation \(n\).
Put
\[
 e_a(M)=MQ^{-a}-M^{-1}\quad(1\le a<N),\qquad
 f_a=\prod_{j=1}^a(1-Q^j),\qquad f_0=1,\qquad
 (b;Q)_a=\prod_{j=0}^{a-1}(1-bQ^j).
 \tag{2}
\]
No formula for a divided outward arrow is used.

Let \(H_M\) be a holomorphic remaining-head seed with
\([K(M),H_M]=0\). H constructs the unique actual total intertwiner
\(W_{H_M}\) having physical highest block \(H_M\), whenever
\(e_1\cdots e_d\ne0\). Its first column is
\[
 C_n(M)=p_nW_{H_M}i_0
       =\frac{(-1)^n}{e_1(M)\cdots e_n(M)}
                         \mathcal L_M^n H_M,
 \qquad \mathcal L_M(X)=K(M)^{-1}[E(M),X].
 \tag{3}
\]
Here \(C_0=H_M\). This is H's physical column, with no factorial
output gauge. All its terminal equations and finite caps are retained.
We may also impose exact integer-degree preservation on the seed.

Write \(E_0=E(1)\), \(K_0=K(1)\), and define F's diagonal frame
on these \(r\) heads by
\[
 h_a(M)=M^{-a}\frac{f_a}{(M^{-2}Q;Q)_a},\qquad
 D_h(M)w_a=h_a(M)w_a,
 \qquad
 A(M)=\bigotimes_{i=1}^r
                \bigl[D_h(M)M^{-(r-i)J_i}\bigr].
 \tag{4}
\]
Here \(J_i\) is the original occupation index. F proves, with
the actual missing endpoint arrows,
\[
 E(M)=A(M)E_0A(M)^{-1},\qquad K(M)=M^rK_0.
 \tag{5}
\]
The frame is diagonal, commutes with \(K_0\), and equals the
identity at \(M=1\). Define
\[
 \widetilde H_M=A(M)^{-1}H_M A(M),\qquad
 \mathfrak A_M(X)=A(M)XA(M)^{-1}.
 \tag{6}
\]
Equations (5) give the exact superoperator identity
\[
          \mathcal L_M=M^{-r}\mathfrak A_M
                         \mathcal L_0\mathfrak A_M^{-1}.
 \tag{7}
\]
In particular the dependence of \(\mathcal L_M\) on \(M\)
has not been omitted.

For any remaining-head matrix \(X\), let its root reference column be
\[
 C_n^0(X)=\frac{(-1)^nQ^{n(n+1)/2}}{f_n}\mathcal L_0^nX,
                      \qquad 0\le n<N.
 \tag{8}
\]
These are fixed-root operators applied to the indicated matrix;
the argument \(X=\widetilde H_M\) below still moves with \(M\).
The identity
\[
 \frac{\prod_{j=1}^n e_j(1)}{\prod_{j=1}^n e_j(M)}
       =M^{-n}\frac{f_n}{(M^{-2}Q;Q)_n}=h_n(M)
 \tag{9}
\]
follows by factoring each denominator as
\(MQ^{-j}(1-M^{-2}Q^j)\). Also
\(\prod e_j(1)=Q^{-n(n+1)/2}f_n\). Substituting (7)--(9) in
(3) proves the full coefficient identity
\[
 \boxed{\quad
 C_n(M)=h_n(M)M^{-rn}
               A(M)C_n^0(\widetilde H_M)A(M)^{-1},
                       \qquad 0\le n<N.
 \quad}\tag{10}
\]
It includes \(n=0\) and \(n=d\). It holds at every level,
including even and composite levels.

For comparison with the ordinary root Euler column, set
\(\Psi_M(t)=\sum_{n=0}^d t^nC_n(M)\).
One has \(\mathcal L_0^N=0\): H's ordered formula gives
\(\mathcal L_0^N=K_0^{-N}\prod_{j=0}^{N-1}(Q^jL_{E_0}-R_{E_0})\),
and the product is a scalar multiple of
\(L_{E_0}^N-R_{E_0}^N=0\). Thus (8) sums to the literal
inverse Euler polynomial \(E_N(Qt\mathcal L_0)^{-1}X\), where
\(E_N(Z)=\sum_{n<N}Z^n/f_n\). Formula (10) does not identify
\(\Psi_M\) with that root polynomial at a fixed unchanged seed.

## 2. Arbitrary diagonal coefficient norms

Use the coefficient-orthonormal Euclidean structure on \(U\).
For \(1\le p\le\infty\), write \(\|\cdot\|_{S_p}\) for the
Schatten norm, including the operator norm at \(p=\infty\).
Let \(w_{n,N}>0\) be any prescribed weights independent of \(\mu\).
They may depend arbitrarily on \(N,n\). Define
\[
 \|\mathbf X\|_{w,p}
       =\left(\sum_{n=0}^d w_{n,N}^{2}
                                  \|X_n\|_{S_p}^{2}\right)^{1/2}.
 \tag{11}
\]
For \(0<\eta<\pi\), F gives polynomial bounds, uniform over
all \(0\le n<N\) and \(|N\mu|\le\eta\), for
\(h_n^{\pm1}\) and \(A^{\pm1}\). These diagonal matrix bounds
hold equally in the present Euclidean basis: their operator
norm is the maximum modulus of a diagonal entry. Moreover
\(|M^{\pm rn}|\le e^{r\eta}\).

Consequently there are \(C,P>0\), depending only on \(r,\eta\),
such that
\[
 \boxed{\quad
 C^{-1}(N+1)^{-P}
       \|\big(C_n^0(\widetilde H_M)\big)_n\|_{w,p}
 \le \|\big(C_n(M)\big)_n\|_{w,p}
 \le C(N+1)^P
       \|\big(C_n^0(\widetilde H_M)\big)_n\|_{w,p}.
 \quad}\tag{12}
\]
The constants do not depend on the weights, seed, or Schatten
index. Indeed \(\|AXB\|_{S_p}\le\|A\|\|B\|\|X\|_{S_p}\).
Apply this to (10), and then to its exact inverse, for each
coefficient; square and sum with the same weights. This proves
both inequalities without summing absolute paths of the braid.

Whenever the two norms are nonzero, their logarithms differ by
\(O(\log(N+1))\). Equivalently, their normalized exponential
rates agree, with the same transformed seed at each \(M\).
No comparison with the seed at \(M=1\) has been made.

## 3. Actual circle norms and the factorial transform

For \(p=2\), the coefficient space is Hilbert. Orthogonality of
the integer Fourier characters gives, exactly, for every \(R>0\),
\[
 \frac1{2\pi}\int_{-\pi}^{\pi}
             \|\Psi_M(Re^{i\theta})\|_{S_2}^{2}\,d\theta
                   =\sum_{n=0}^d R^{2n}\|C_n(M)\|_{S_2}^{2}.
 \tag{13}
\]
Thus (12) with \(w_{n,N}=R^n\) compares the actual circle
\(L^2\) norm with the root reference column of \(\widetilde H_M\)
on that same circle. The estimate is uniform even if the chosen
radius depends on \(N\); only positivity of the weights was used.

The factorial output column is the finite polynomial
\[
 \mathscr B_M(z)=\sum_{n=0}^d\frac{z^n}{f_n}C_n(M)
   =\frac1{2\pi i}\oint
                \Psi_M(\zeta)E_N(z/\zeta)\,\frac{d\zeta}{\zeta}.
 \tag{14}
\]
Any positively oriented circle about zero proves this identity
by taking the constant coefficient of the finite Laurent product.
Every endpoint of both polynomials remains. It is the actual
factorial output change, not a coherent inverse-symbol rule.
Its exact circle norm is
\[
 \frac1{2\pi}\int_{-\pi}^{\pi}
          \|\mathscr B_M(Re^{i\theta})\|_{S_2}^{2}\,d\theta
             =\sum_{n=0}^d\frac{R^{2n}}{|f_n|^2}
                                         \|C_n(M)\|_{S_2}^{2}.
 \tag{15}
\]
Taking \(w_{n,N}=R^n/|f_n|\) in (12) gives the same polynomial
equivalence for this entire transformed column. No assumption
that the factorial weights themselves have polynomial size is
needed: the identical weights occur on both sides.
Parseval is used only for the Hilbert--Schmidt norm here; no
corresponding equality for a non-Hilbert Schatten norm is asserted.

## 4. True meridian jets, including the moving seed

Choose \(0<\eta<\eta'<\pi\), and suppose \(H_M\) is holomorphic
on a neighborhood of the larger closed scaled disk. Regard
(10) as an invertible diagonal-block map \(\mathcal T_{N,\mu}\)
on the arrays in (11). Its inverse has blocks
\(X_n\mapsto h_n(M)^{-1}M^{rn}A(M)^{-1}X_nA(M)\).
The preceding bounds hold on the larger disk in either direction.
Cauchy's formula therefore gives, for every fixed \(k\),
\[
 \|\partial_\mu^k\mathcal T_{N,\mu}^{\pm1}\|_{w,p\to w,p}
                       \le C_k N^k(N+1)^P
                  \quad (|N\mu|\le\eta).
 \tag{16}
\]
This is uniform in the weights, since the maps do not mix degrees.
The same bounds follow directly by differentiating their finite
diagonal blocks. All derivatives are at fixed \(q_N\).

For a fixed integer \(k_*\ge0\), define the scaled jet norm
\[
 \|\mathbf X\|_{w,p;k_*}
   =\left(\sum_{k=0}^{k_*}N^{-2k}
                    \|\partial_\mu^k\mathbf X\|_{w,p}^{2}\right)^{1/2}.
 \tag{17}
\]
The product rule in both directions in (10), followed by the
finite-dimensional Cauchy--Schwarz inequality in the jet index,
proves (12) with this jet norm in place of \(\|\cdot\|_{w,p}\),
with possibly larger constants and exponent. The reference jet
is explicitly
\[
 \partial_\mu^k C_n^0(\widetilde H_M)
                         =C_n^0(\partial_\mu^k\widetilde H_M).
 \tag{18}
\]
It is not the root column of an undifferentiated seed.
Equations (13),(15) apply to each jet as well, since their
Fourier factors and factorials are fixed in \(\mu\).

Here is the exact first normal in a form that records the frame.
Let \(\mathcal H=A'(1)\), where the prime means \(\partial_\mu\)
at zero. F evaluates it as
\[
 \mathcal H=\sum_{i=1}^r
     \left[-(r-i+1)J_i-2\sum_{a=1}^{J_i}\frac{Q^a}{1-Q^a}\right].
 \tag{19}
\]
Also
\[
 \sigma_n=\left.\partial_\mu h_n(e^\mu)\right|_0
       =-n-2\sum_{a=1}^n\frac{Q^a}{1-Q^a}
       =\sum_{a=1}^n\coth(\pi i a/N),\qquad \sigma_0=0.
 \tag{20}
\]
Write \(H_0=H_M|_{M=1}\),
\(H_1=\left.\partial_\mu H_{e^\mu}\right|_0\),
\(C_{n,0}=C_n^0(H_0)\), and
\(C_{n,1}=\left.\partial_\mu C_n(e^\mu)\right|_0\).
Then (10) gives
\[
 \boxed{\quad
 C_{n,1}=(\sigma_n-rn)C_{n,0}
       +[\mathcal H,C_{n,0}]
       +C_n^0\bigl(H_1-[\mathcal H,H_0]\bigr).
 \quad}\tag{21}
\]
Both the operator frame and the seed normal are present.
In particular the polynomial norm statement is not obtained by
differentiating a root-only coherent principal symbol.

## 5. Original source and the endpoint still to estimate

H's original pointed source is exactly
\[
 \Phi_0(W_{H_M})=\operatorname{Tr}_U(K(M)^{1-N}H_M)
               =\operatorname{Tr}_U(K(M)^{1-N}\widetilde H_M).
 \tag{22}
\]
The second equality uses commutation of the diagonal frame with
the pivot. Its first normal is
\(\operatorname{Tr}(K_0^{1-N}(H_1-rdH_0))\); all external
crossing, framing and peripheral scalar lines remain in the seed
or are multiplied with their own derivatives. Formula (10) is a
presentation of this same finite completion, not a replacement
of its highest cut by a norm.

The protected bulk Gamma asymptotic of shifted factorials is
already covered by research_balanced_gauss_cardinal_reconstruction.md,
and F already gives the whole-cap polynomial frame bound used here.
Neither scalar estimate is claimed as new. The conclusion here is
their exact completion interface (10) and the uniform whole-column
Fourier and jet norm comparisons for arbitrary diagonal weights.

In particular (15) controls meridian transport of an actual
factorial-transformed norm, but does not initialize its local
endpoint at infinity. With
\(\widehat\Psi_M(w)=w^d\Psi_M(w^{-1})\), (14) also equals
\([w^d](\widehat\Psi_M(w)E_N(zw))\). The reciprocal column has
constant coefficient \(C_d(M)\) and neighboring coefficients
\(C_{d-k}(M)\); these remain actual seed-dependent matrices.
A circle norm is not a nonzero value at this endpoint, a relative
estimate after contraction, or a selected original cycle coefficient.
No claim about a geometric coherent window or a closed-source lower
bound follows from (12)--(22).

## Complete proof-source pins

* H: notes/research_physical_highest_block_endpoint_coordinates.md,
  453 lines, SHA256
  deaadaa899cdb08aefbbcb1e1ca87a40f84a1ade608fceeeaba6426027bd9b1b.
* F: notes/research_actual_meridian_source_frames.md,
  506 lines, SHA256
  6f58fba195ba5e8208e1d5180a1d684b933f9f5d50eb28efc56609580fe29976.

Both complete directs were freshly read nontruncated in this active
author sequence. Every used source and frame implication was checked.
Only written mathematics and text/hash operations were used. Frozen
files, public manuscripts and the progress ledger were not changed.
