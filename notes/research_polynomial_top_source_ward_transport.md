# Polynomial Ward transport to the literal top source

Private written proof, 19 November 2026.

The original highest-cut pivotal source differs from a specified top
matrix coefficient by an explicit two-head \(E\)-current. Its primitive
has norm \(O(N)\) at the root and polynomial norm, including all fixed
true meridian jets, on a scaled meridian disk. The operator exponent
does not grow with the number of spectator heads. No inverse of the
full commutator operator is used.

The sole complete direct F supplies the actual finite head matrices,
ordered coproduct, original pointed pivot, and meridian diagonal frame.
The primitive, top coupon, source identity, and bounds below are proved
inline. All norms below use the physical coefficient Euclidean metric:
the displayed vectors \(w_a\) are orthonormal, with tensor-product
metrics. No estimate in a different coherent or binomial metric is
inferred. F's diagonal conditioning bounds are unchanged in this metric.

## 1. Finite matrices and the claimed source comparison

Fix \(N\ge2\), \(d=N-1\), \(m\ge2\),
\[
 q=e^{\pi i/N},\qquad Q=q^2,\qquad M=e^\mu,\qquad
 x=-M/q,\qquad x_0=-q^{-1}.
 \tag{1}
\]
The quantum root stays fixed. On \(V=\operatorname{span}\{w_0,\ldots,w_d\}\),
write \(Jw_b=bw_b\), and use the actual arrows
\[
 E(M)w_b=(MQ^{-b}-M^{-1})w_{b-1}\quad(b>0),\quad E(M)w_0=0,
 \qquad K(M)w_b=xQ^{-b}w_b.
 \tag{2}
\]
In particular the missing bottom arrow is zero also off the root.
Put \(Z=V^{\otimes(m-2)}\), and let \(K_Z,E_Z\) be its ordered
Cartan and lowering coproduct. For \(m=2\), \(Z=\mathbb C\),
\(K_Z=I\), and \(E_Z=0\). Then
\[
 E_{12}=E_1K_2+E_2,\qquad E_\Sigma=E_{12}K_Z+E_Z.
 \tag{3}
\]
Here and below tensor identities in coproduct formulas are implicit.
Let \(P_0=|0\rangle\langle0|\), and set
\[
 \begin{split}
 O&=|0\rangle\langle d|\otimes|d\rangle\langle0|,\\
 Q_{\rm pt}(M)&=P_0\otimes K_2(M)^{-d}\otimes K_Z(M)^{-d},\\
 Q_{\rm top}(M)&=O\otimes K_Z(M)^{-d},\\
 \Phi_M(C)&=\operatorname{Tr}(Q_{\rm pt}(M)C).
 \end{split}\tag{4}
\]
This is F's original highest-cut pivot. Any original crossing scalar,
zero-framing factor, or prescribed mark remains inside \(C\), or is
retained as an explicit outside scalar with its product rule.

We will construct a holomorphic matrix \(\mathcal A(M)\) satisfying
\[
 [\mathcal A(M),E_\Sigma(M)]=Q_{\rm pt}(M)-Q_{\rm top}(M).
 \tag{5}
\]
It follows for every full matrix \(C\), with no intertwining hypothesis,
that
\[
 \boxed{\quad
 \Phi_M(C)=\operatorname{Tr}(Q_{\rm top}C)
                 +\operatorname{Tr}\bigl(\mathcal A[E_\Sigma,C]\bigr).
 \quad}\tag{6}
\]
Indeed \(\operatorname{Tr}([\mathcal A,E_\Sigma]C)
=\operatorname{Tr}(\mathcal A(E_\Sigma C-CE_\Sigma))\).
The top term is the literal coefficient
\[
 \operatorname{Tr}(Q_{\rm top}C)
 =\operatorname{Tr}_Z\!\left[
 K_Z^{-d}\langle d,0|C|0,d\rangle\right].
 \tag{7}
\]
No ribbon cut move or replacement of a marked source by an unmarked
scalar trace is needed to obtain (6).

## 2. An explicit capped two-head primitive at the root

Define the unit raising shift \(Rw_b=w_{b+1}\) for \(b<d\),
\(Rw_d=0\). This \(R\) is not a braid crossing or the physical \(F\).
Write \(E_0=E(1)\), \(K_0=K(1)\). For \(1\le n\le N\),
\[
 [R^n,E_0]=(1-Q^{-n})x_0^{-1}R^{n-1}K_0.
 \tag{8}
\]
Here is the cap check. In the interior the coefficient on \(w_b\) is
\((Q^{-b}-1)-(Q^{-b-n}-1)=Q^{-b}(1-Q^{-n})\).
At \(b=0\) the same identity uses the actual zero bottom arrow,
\(Q^0-1=0\). At \(b+n=N\), it uses \(Q^{-N}-1=0\), which is
only a root coefficient identity, not an added arrow. For \(b+n>N\)
both products on the left and \(R^{n-1}w_b\) vanish. For \(n=N\)
both sides vanish. Thus (8) includes every finite endpoint.

For \(0\le a<d\), put
\[
 \lambda_a=\frac{x_0^{a-d}}{1-Q^{-a-1}},\qquad
 X_a=\lambda_aR^{a+1},\qquad
 \mathcal A_{12,0}=\sum_{a=0}^{d-1}|0\rangle\langle a|\otimes X_a.
 \tag{9}
\]
All denominators are nonzero. Set \(X_{-1}=X_d=0\) and
\(e_a=Q^{-a}-1\). The only possibly nonzero first-head row of
\([\mathcal A_{12,0},E_{12,0}]\) is row zero. Its column \(a\) is
\[
 [X_a,E_0]+e_aX_{a-1}K_0.
 \tag{10}
\]
For \(a=0\), (8) makes this
\[
 \lambda_0(1-Q^{-1})x_0^{-1}K_0
       =x_0^{-N}K_0=K_0^{-d},
 \tag{11}
\]
where \(K_0^N=x_0^NI\). For \(1\le a<d\), the coefficient of
\(R^aK_0\) is zero because
\[
 \lambda_a(1-Q^{-a-1})x_0^{-1}=x_0^{a-d-1},\qquad
 e_a\lambda_{a-1}=-x_0^{a-d-1}.
 \tag{12}
\]
At \(a=d\), \(e_d=Q-1\),
\(\lambda_{d-1}=x_0^{-1}/(1-Q)\), and
\(R^dK_0=x_0|d\rangle\langle0|\). Consequently the top column
of (10) is \(-|d\rangle\langle0|\). This proves exactly
\[
 [\mathcal A_{12,0},E_{12,0}]
       =P_0\otimes K_0^{-d}-O.
 \tag{13}
\]
The argument also applies when \(N=2\), when the middle range is empty.

The matrix in (9) has integer occupation degree \(+1\): its first
head changes by \(-a\), and its second by \(a+1\). Its range is
\(|0\rangle\otimes\operatorname{span}\{w_1,\ldots,w_d\}\), of
dimension \(d\); the \(a=0\) block already covers this range.
Row-block Cauchy--Schwarz and \(\|R^j\|\le1\) give
\[
 \|\mathcal A_{12,0}\|
 \le\left(\sum_{j=1}^{N-1}|1-Q^{-j}|^{-2}\right)^{1/2}
 \le\frac N2.
 \tag{14}
\]
For the last bound, use
\(|1-Q^j|\ge4\min(j,N-j)/N\) and
\(\sum_{j=1}^{N-1}\min(j,N-j)^{-2}\le
2\sum_{j\ge1}j^{-2}\le4\), the latter following from the
integral comparison \(\sum_{j\ge1}j^{-2}\le2\).
Thus, for \(1\le p<\infty\),
\[
 \|\mathcal A_{12,0}\|_{S_p}\le d^{1/p}N/2.
 \tag{15}
\]

## 3. The actual meridian extension and spectator tensor

Use F's diagonal one-head frame
\[
 h_b(M)=M^{-b}\frac{(Q;Q)_b}{(M^{-2}Q;Q)_b},\qquad
 D_h(M)w_b=h_b(M)w_b,
 \tag{16}
\]
where \((z;Q)_b=\prod_{j=0}^{b-1}(1-zQ^j)\).
Its consecutive ratio proves \(E(M)=D_hE_0D_h^{-1}\), including
the forced bottom. The two-head lowering frame is
\[
 \mathcal D_{12}(M)=(D_h(M)M^{-J_1})\otimes D_h(M),\qquad
 E_{12}(M)=\mathcal D_{12}E_{12,0}\mathcal D_{12}^{-1}.
 \tag{17}
\]
The first-head \(M^{-J_1}\) supplies the factor \(M\) in \(K_2(M)\).
This diagonal frame fixes \(P_0\otimes K_0^{-d}\), while
\[
 \mathcal D_{12}O\mathcal D_{12}^{-1}=M^dO,
 \tag{18}
\]
since its entries at \((0,d)\) and \((d,0)\) are respectively
\(h_d\) and \(h_dM^{-d}\). Therefore
\[
 \mathcal A_{12}(M)=M^{-d}\mathcal D_{12}(M)
                    \mathcal A_{12,0}\mathcal D_{12}(M)^{-1}
 \tag{19}
\]
satisfies
\[
 [\mathcal A_{12}(M),E_{12}(M)]=P_0\otimes K_2(M)^{-d}-O.
 \tag{20}
\]
This is a whole-\(M\) identity wherever the displayed frame is a unit,
not a derivative of an off-root continuation of (8).

For the spectator tensor, at the fixed quantum root,
\(K_Z(M)^N=x^{N(m-2)}I\). Hence \(K_Z^{-N}\) is a scalar matrix
and commutes with \(E_Z\). Define
\[
 \boxed{\quad \mathcal A(M)=\mathcal A_{12}(M)\otimes K_Z(M)^{-N}.
 \quad}\tag{21}
\]
Equations (3),(20) give
\[
 [\mathcal A,E_\Sigma]
 =[\mathcal A_{12},E_{12}]\otimes K_Z^{1-N}
 =Q_{\rm pt}-Q_{\rm top},
 \tag{22}
\]
proving (5)--(7). No identity at an off-grid Cartan parameter is used.
The degree of \(\mathcal A\) remains \(+1\). In particular, if \(C\)
has degree zero, then \([E_\Sigma,C]\) has degree \(-1\), and its
trace pairing with \(\mathcal A\) need not vanish. Degree averaging
does not discard the current in (6).

## 4. Polynomial collar bounds with explicit dimension costs

Fix \(0<\eta<\eta'<\pi\), with \(m\) fixed. F's complete
whole-cap estimate gives, uniformly for \(0\le b<N\) and
\(|N\mu|\le\eta'\),
\[
 (N+1)^{-C_{\eta'}}\le|h_b(e^\mu)|\le(N+1)^{C_{\eta'}}.
 \tag{23}
\]
The matrices and their inverses are holomorphic on this disk.
The Cartan factors \(M^{-J_1}\) and \(M^{-d}\) in (19) have bounded
modulus and inverse there. Thus one may take
\(P_{\eta'}=1+4C_{\eta'}\), increasing constants when necessary,
such that
\[
 \sup_{|N\mu|\le\eta'}\|\mathcal A_{12}(e^\mu)\|
       \le C_{\eta'}(N+1)^{P_{\eta'}}.
 \tag{24}
\]
The exponent is independent of \(m\). The spectator scalar has
modulus at most \(e^{(m-2)\eta'}\); it affects only the constant.
Cauchy estimates on the buffered scaled disk consequently imply
\[
 \sup_{|N\mu|\le\eta}
 \|\partial_\mu^k\mathcal A(e^\mu)\|
 \le C_{m,\eta,\eta',k}N^k(N+1)^{P_{\eta'}}
 \qquad(k\ge0\text{ fixed}).
 \tag{25}
\]
Every derivative has range in the same subspace
\(|0\rangle\otimes\operatorname{span}\{w_1,\ldots,w_d\}\otimes Z\).
Its rank is at most \(dN^{m-2}\). Therefore (25) gives
\[
 \|\partial_\mu^k\mathcal A\|_{S_p}
 \le (dN^{m-2})^{1/p}
       C_{m,\eta,\eta',k}N^k(N+1)^{P_{\eta'}}.
 \tag{26}
\]
At \(\mu=0\), the spectator scalar has modulus one, and the sharper
root estimates are
\[
 \|\mathcal A_0\|\le N/2,\qquad
 \|\mathcal A_0\|_{S_p}\le(dN^{m-2})^{1/p}N/2,
 \qquad \|\mathcal A_0\|_1\le N^m/2.
 \tag{27}
\]
Also \(Q_{\rm top}\) has rank \(N^{m-2}\) and norm
\(|M|^{-(m-2)d}\). These statements include the empty spectator case.
There is no Laurent pole at \(\mu=0\) in either source coupon or in
\(\mathcal A\).

For an analytic marked matrix \(C(M)\), write \(Y=[E_\Sigma,C]\)
and \(\Delta=\Phi_M(C)-\operatorname{Tr}(Q_{\rm top}C)\).
Trace duality gives the actual current bounds
\[
 \begin{split}
 |\Delta|&\le C_{m,\eta'}(N+1)^{P_{\eta'}}\|Y\|_1,\\
 |\Delta|&\le C_{m,\eta'}N^{m-1}(N+1)^{P_{\eta'}}\|Y\|,\\
 |\Delta|&\le C_{m,\eta'}N^{(m-1)/2}(N+1)^{P_{\eta'}}\|Y\|_2.
 \end{split}\tag{28}
\]
At the root the respective factors may instead be taken as
\(N/2\), \(N^m/2\), and \((N/2)(dN^{m-2})^{1/2}\).
For fixed \(k\), the product rule and (25) give, on the smaller disk,
\[
 N^{-k}|\partial_\mu^k\Delta|
 \le C_{m,\eta,\eta',k}(N+1)^{P_{\eta'}}
       \sum_{\ell=0}^kN^{-\ell}\|\partial_\mu^\ell Y\|_1.
 \tag{29}
\]
The operator-norm version has the extra factor \(N^{m-1}\), and the
Hilbert--Schmidt version the extra factor \(N^{(m-1)/2}\).
All quantities are full finite matrices in the stated metric.
An \(O(N^{-k})\) current can therefore suffice for an absolute error
after paying the displayed powers; its order, scalar normalization,
and the desired error scale must be checked. A small normalized
coherent kernel is not by itself a bound for any norm in (28).

For example, suppose at the root that \(L_N\ne0\),
\(\operatorname{Tr}(Q_{{\rm top},0}C_N)=L_N(1+o(1))\), and the
actual trace-norm current satisfies
\[
 \|[E_{\Sigma,0},C_N]\|_1\le\varepsilon_N|L_N|/N.
 \tag{29a}
\]
Then (27) proves
\(\Phi_{M=1}(C_N)=L_N(1+o(1)+O(\varepsilon_N))\). In particular a
bound \(|L_N|N^{-2}\) for this current contributes relative
error \(O(N^{-1})\). The operator-norm version requires
\(\|[E_{\Sigma,0},C_N]\|\le\varepsilon_N|L_N|N^{-m}\).
Thus this comparison has polynomial, rather than exponential, norm
loss. The assumed norm control is a substantial input; the statement
does not assert it for a geometric localization or after a coherent
contraction. An outside scalar multiplies both compared terms and
retains its derivatives.

## 5. The true first normal and exact scope

For explicit first jets, set
\[
 \Sigma_{a,N}=\sum_{j=1}^a\frac{Q^j}{1-Q^j},\qquad
 \mathcal H_{12}=-2J_1-J_2-2\Sigma_{J_1,N}-2\Sigma_{J_2,N}.
 \tag{30}
\]
F's exact derivative of (16) gives
\(\left.\partial_\mu\mathcal D_{12}(e^\mu)\right|_0=\mathcal H_{12}\).
Differentiating (19),(21) in the actual fixed-\(q\) family proves
\[
 \mathcal A_1=
 \bigl([\mathcal H_{12},\mathcal A_{12,0}]
       -(d+N(m-2))\mathcal A_{12,0}\bigr)\otimes K_{Z,0}^{-N}.
 \tag{31}
\]
Subscripts 0 and 1 denote value and \(\partial_\mu\) at zero.
The two pivot derivatives are
\(Q_{{\rm pt},1}=-d(m-1)Q_{{\rm pt},0}\) and
\(Q_{{\rm top},1}=-d(m-2)Q_{{\rm top},0}\). Put
\[
 Y_0=[E_{\Sigma,0},C_0],\qquad
 Y_1=[E_{\Sigma,1},C_0]+[E_{\Sigma,0},C_1].
 \tag{32}
\]
The complete first-normal source identity is
\[
 \begin{split}
 \operatorname{Tr}Q_{{\rm pt},0}(C_1-d(m-1)C_0)
 &=\operatorname{Tr}Q_{{\rm top},0}(C_1-d(m-2)C_0)\\
 &\quad+\operatorname{Tr}(\mathcal A_1Y_0+\mathcal A_0Y_1).
 \end{split}\tag{33}
\]
Higher fixed jets use (6) directly. They require only the corresponding
actual derivatives of \(C,E_\Sigma,\mathcal A\), with no extra Laurent
coefficient. Any retained outside scalar is differentiated as well.
If \(C(M)\) commutes with \(E_\Sigma(M)\) throughout the meridian
family, all current terms vanish. Root-only commutation eliminates
\(Y_0\) but does not eliminate \(Y_1\).

Thus the top coefficient agrees with the original source on actual
total intertwiners, and for arbitrary marked matrices its discrepancy
is one explicit polynomially bounded Ward functional. This is a
source comparison, not an assertion that a chosen geometric window
has a small current. It neither constructs such a window nor supplies
a geometric relative-cycle coefficient, a relative phase comparison,
or a nonzero closed-source lower bound. The separate opposite-
polarization return is not identified with this two-head primitive.
No new volume-conjecture case follows from these identities alone.

## Complete proof direct and verification record

* F: `notes/research_actual_meridian_source_frames.md`, 506 lines,
  SHA256 `6f58fba195ba5e8208e1d5180a1d684b933f9f5d50eb28efc56609580fe29976`.

The complete direct was freshly read nontruncated in three covering
chunks during this author sequence. All used identities and bounds
were checked, including the original pivot and the actual bottom-zero
meridian frame. The new two-head proof does not use an estimate for a
general commutator inverse. Only written mathematics and text/hash
operations were used; no mathematical programs or numerical tests
were run. Frozen and public sources were not edited.
The entire final was freshly reread nontruncated after the last
presentation corrections; its sole direct pin was renewed and matched.
