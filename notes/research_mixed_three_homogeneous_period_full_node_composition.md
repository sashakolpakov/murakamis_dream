# Homogeneous conditional periods at every physical node

Research deduction, 7 November 2026. The contour-defined particular
current of the twice-crossed source extends, at each fixed level, to a
product of strips containing **all** incoming and outgoing physical
nodes. Its homogeneous remainder therefore represents the actual
power-two block in a complete finite contraction. Two adjacent such
blocks have an explicit intervening matrix; the physical turn is not
removed.

This is an exact composition result. The extension near the endpoint
nodes is not asserted to have an \(N\)-uniform estimate. No geometric
action, dominance, or nonzero asymptotic for the composed observation
is inferred. No numerical evaluation is used.

## 1. The same current on a larger fixed-level domain

Fix \(N\ge2\), and put
\[
 D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
 P_j=(r;r)_j,\quad \kappa=q^{D^2/2},\quad
 X=e^{-2\pi ia},\quad W=e^{-2\pi iy}.
 \tag{1}
\]
Let
\[
 \mathcal S_N=\{z\in\mathbb C:-1/(2N)<\Re z<1\},\qquad
 \alpha_N=-1/(2N).
 \tag{2}
\]
Use the literal source and original factorial row of
[the particular-current theorem](research_mixed_three_fourier_conditional_particular_current.md),
equations (1)--(2):
\[
\begin{split}
 F_N(a,y)&=C_{0,N}(X,W)
   =\sum_{j=0}^{D}\frac{X^{-j}(rX;r)_j(rW;r)_j}{P_j^2},\\
 T_N(s;a,y)&=e^{2\pi iNas}
   \Pi_N(s+a)\Pi_N(s+y)E_N(a)E_N(y)E_N(s)^2 .
\end{split}
 \tag{3}
\]
The same note defines
\[
 k_{3,N}(s)=\frac{t(1+t)}{(1-t)^3},\quad t=e^{-2\pi iNs},
 \qquad
 A_N(a,y)=\frac{N^3}{2}
   \int_{\alpha_N-i\infty}^{\alpha_N+i\infty}
                          k_{3,N}(s)T_N(s;a,y)\,ds .
 \tag{4}
\]
The line is oriented upward. The symbol \(A_N\) in (4) is a scalar
current coefficient, distinct from the crossing matrices \(A_n=JM^n\)
used below.

**Proposition 1.** At each fixed \(N\), (4) is absolutely convergent
and holomorphic on \(\mathcal S_N^2\). It extends the very same
current defined on the earlier parameter domain.

*Proof.* On the integration line, the numerator arguments satisfy
\[
 \Re(s+a)>-1/N,\qquad \Re(s+y)>-1/N.
\]
The reciprocal arguments \(a,y,s\) have real parts less than one.
Thus every factor is holomorphic by
[the joint global chart](research_mixed_fourier_right_cap_joint_global_chart.md),
Section 1. In particular the positive support walls of \(\Pi_N\)
remain zeros, and no quotient by such a zero is used.
The kernel has no pole on this line, since
\(t=-e^{2\pi N\Im s}<0\).

The exact fixed-level factorial asymptotics in
[factorial alias elimination](research_mixed_fourier_factorial_alias_elimination.md),
equations (4)--(6), give, uniformly when \((a,y)\) lies in a fixed
compact subset of \(\mathcal S_N^2\),
\[
\begin{split}
 T_N(s;a,y)&=E_N(a)E_N(y)e^{2\pi iNas}(1+o(1)),
                                      &&\Im s\longrightarrow-\infty,\\
 T_N(s;a,y)&=D_N(a,y)e^{-2\pi iNys}(1+o(1)),
                                      &&\Im s\longrightarrow+\infty,
\end{split}
 \tag{5}
\]
where the original constant is
\[
 D_N(a,y)=E_N(a)E_N(y)
  \exp\{i\pi[N(a+y-a^2-y^2)-(a+y)]\}.
 \tag{6}
\]
These are the same polynomial exponent identities as (8)--(10) of
[the endpoint-current proof](research_mixed_three_fourier_conditional_endpoint_current.md).
Their fixed-level derivation needs the stated factorial domains,
not the earlier inequalities \(\Re a,\Re y<1/2\) or \(\Im y>0\).
On the two ends of the midpoint line, the kernel in (4) has modulus
\(O_N(e^{-2\pi N|\Im s|})\). Consequently its product with the row
decays at respective rates
\[
 e^{-2\pi N(1-\Re a)H},\qquad
 e^{-2\pi N(1-\Re y)H}\qquad(H\longrightarrow+\infty).
 \tag{7}
\]
Both exponents are strictly negative and locally uniformly so on
\(\mathcal S_N^2\). This proves absolute convergence and supplies
locally uniform integrable majorants. It also proves holomorphy.
On the original domain (4) has exactly the original integrand and
contour, so no new normalization or periodic ambiguity is introduced.
\(\square\)

The constants in this proof may depend on \(N\) and the compact set.
In particular (7) is not a uniform large-\(N\) estimate on a family
whose real coordinates approach zero or one.

Define throughout the new domain
\[
 F_N^{\rm part}(a,y)
   =\frac{(1-W^N)(X^{-N}-1)}{N^2}A_N(a,y),
 \qquad H_N(a,y)=F_N(a,y)-F_N^{\rm part}(a,y).
 \tag{8}
\]
These are holomorphic functions on \(\mathcal S_N^2\). The incoming
homogeneous equation has its usual shifted-domain qualification:
\[
 \mathcal L_{N,W}H_N=0
 \quad\text{when}\quad
 -1/(2N)<\Re a<1-2/N,\qquad y\in\mathcal S_N,
 \tag{9}
\]
where \(\mathcal L_{N,W}\) is the original operator in (4) of the
particular-current theorem.

For clarity, (9) also follows directly from the existing telescoper
proof, without imposing an equation at arguments outside the new
domain. All shifts \(a,a+1/N,a+2/N\) then lie in \(\mathcal S_N\).
In shifting its vertical line by \(1/N\), the lower connector for
\((e^{2\pi is}-1)^2T_N(s)\) decays with exponent
\(2\pi[N(1-\Re a)-2]>0\); the upper connector decays with
\(2\pi N(1-\Re y)>0\). The only kernel pole remains \(s=0\),
where \(T_N(0)=1\), and its residue is unchanged. Thus
\(\mathcal L_{N,W}A_N=-1\), giving (9).
No cyclic equation at the last two sampled arguments is asserted.

## 2. Every node, including the two omitted ends

All points \(b/N\), \(0\le b<N\), lie strictly inside \(\mathcal S_N\).
The exact factors in (8) therefore prove
\[
\begin{split}
 H_N(b/N,y)&=C_{0,N}(r^b,e^{-2\pi iy}),
                                      &&y\in\mathcal S_N,\\
 H_N(a,l/N)&=C_{0,N}(e^{-2\pi ia},r^l),
                                      &&a\in\mathcal S_N.
\end{split}
 \tag{10}
\]
These are identities of holomorphic functions in the unsampled
variable. They include \(b=0,l=0\), both middle parities, and
\(b=N-1,l=N-1\); no endpoint limit is required.

In particular define the full \(N\times N\) matrix
\[
 \mathbf H_N=(H_N(b/N,l/N))_{0\le b,l<N}.
 \tag{11}
\]
Its entries are exactly
\[
 (\mathbf H_N)_{bl}
   =\sum_{j=0}^{\min(D-b,D-l)}
       \frac{r^{-bj}P_{b+j}P_{l+j}}{P_bP_lP_j^2}.
 \tag{12}
\]
The two triangular support walls follow from the actual factors
\((r^{b+1};r)_j\) and \((r^{l+1};r)_j\). All denominators in
(12) are nonzero.
At the common endpoint this gives the finite nonzero anchor
\[
                         H_N(0,0)=N.
 \tag{13}
\]
Equation (13) is not a saddle or a geometric growth assertion.

The normal information is not deleted. For example at interior
physical pairs, differentiating the factors in (8) gives
\[
 \partial_a\partial_yF_N^{\rm part}(b/N,l/N)
                              =-4\pi^2 A_N(b/N,l/N).
 \tag{14}
\]
Individual first derivatives vanish when both variables are sampled,
but the mixed derivative need not vanish. Thus (10) does not
license replacing raw derivatives of \(C_0\) by raw derivatives
of \(H_N\) in an arbitrary Hermite observation.

## 3. The actual power-two block with its entire incoming state

Retain the original Fourier cardinal vector \(h(y)\), Newton crossing
\(M\), reversal \(J\), and
\[
 A_2=JM^2,\qquad
 f=Sh,\qquad
 S=\operatorname{diag}
    \left(\frac{\kappa^{-1}(-q)^{-b}}{P_b}\right)M.
 \tag{15}
\]
These are the original matrices from
[exact wire contraction](research_mixed_wire_exact_contraction.md).
Let \(\ell^T\) be any original incoming coefficient row, with other
boundary variables allowed in its entries.
For either \(\eta=0,1\), define the unique polynomial \(F\) of
degree less than \(N\) by
\[
                 P_b^{1-\eta}F(r^b)=(\ell^TS^{-1})_b.
 \tag{16}
\]
Equivalently \(\mathcal E_\eta F=\ell^Th\) under the proved
[conditional/Fourier bridge](research_mixed_conditional_fourier_message_bridge.md).

**Theorem 2.** On \(y\in\mathcal S_N\), the full original adjacent
power-two attachment is
\[
 \boxed{\quad
 \ell^TA_2h(y)
   =e^{\pi iDy}\sum_{b=0}^{D}
               \frac{F(r^b)}{P_b^\eta}H_N(b/N,y)
   =e^{\pi iDy}\sum_{b=0}^{D}
               \frac{(\ell^TS^{-1})_b}{P_b}H_N(b/N,y).
 \quad}
 \tag{17}
\]
It holds for the row of any actual preceding short path or branching
context, using that context's unchanged original coefficients.

*Proof.* The exact last-four attachment, from the bridge and literal
terminal source, is
\[
 \ell^TA_4h(y)
    =\kappa^2N\sum_{b=0}^{D}
                         \frac{F(r^b)}{P_b^\eta}Z_N(b/N,y).
 \tag{18}
\]
Apply the original two negative output crossings. The left side is
\(\ell^TA_4M^{-2}h=\ell^TA_2h\), with the physical reversal
still present. The complete negative-crossing identity gives
\[
 \mathcal M_{-2}Z_N(a,y)
           =\frac{\kappa^{-2}e^{\pi iDy}}N
                         C_{0,N}(e^{-2\pi ia},e^{-2\pi iy}).
 \tag{19}
\]
The scalar \(\kappa^2N\) in (18) cancels the exact
\(\kappa^{-2}/N\) in (19). Now use (10) at **every** incoming
node, which proves (17).
The \(\eta=1\) form of (18) already includes both original
constant-term sectors; they have not been identified individually.
\(\square\)

For a positive three/four prefix of length \(m\ge2\), with the last
four replaced by two,
let its old flags be \(\epsilon_1,\ldots,\epsilon_m\), with
\(\epsilon_m=1\), \(k=\sum\epsilon_j\), \(\eta=\epsilon_{m-1}\),
and \(F_{m-1}\) its original conditional prefix. Formula (17) reads
\[
\begin{split}
 &v(w)^TA_{3+\epsilon_1}\cdots A_{3+\epsilon_{m-1}}A_2h(y)\\
 &\quad=\kappa^{m+k-2}N^{k-1}e^{\pi iDy}
       \sum_{b=0}^{D}\frac{F_{m-1}(r^b)}{P_b^\eta}H_N(b/N,y)\\
 &\quad=\kappa^{m+k-2}N^{k-1}e^{\pi iDy}
       \sum_{\substack{b,j\ge0\\b+j<N}}
       \frac{F_{m-1}(r^b)r^{-bj}P_{b+j}
                  (re^{-2\pi iy};r)_j}{P_b^{1+\eta}P_j^2}.
\end{split}
 \tag{20}
\]
This is the concrete remaining coherent sum. Neither its original
prefix phase nor its triangular support may be discarded.

## 4. Two adjacent homogeneous blocks and the actual interface

Write
\[
 \mathsf P=\operatorname{diag}(P_b),\qquad
 \mathsf D=\operatorname{diag}(e^{\pi iDb/N})
            =\operatorname{diag}((-q)^{-b}).
 \tag{21}
\]
Evaluating (17) at every outgoing node gives the complete matrix
identity
\[
 \boxed{\qquad A_2=S^{-1}\mathsf P^{-1}\mathbf H_N\mathsf D.\qquad}
 \tag{22}
\]
There is no semisimple quotient in (22). The \(h\)-node coordinates
are a full basis for the original \(N\)-dimensional Fourier state.

In particular two adjacent power-two components satisfy
\[
 \boxed{\quad
 A_2^2
   =S^{-1}\mathsf P^{-1}\mathbf H_N\mathsf B_N
                            \mathbf H_N\mathsf D,\qquad
 \mathsf B_N=\mathsf D S^{-1}\mathsf P^{-1}
                  =\kappa\mathsf D M^{-1}\mathsf D^{-1}.
 \quad}
 \tag{23}
\]
The last equality follows directly from (15). Thus \(\mathsf B_N\)
is a specified original negative-crossing interface, conjugated only
by the displayed diagonal phases. It is lower triangular in the
original index order. It is not the identity, a conjugate pairing,
or pointwise multiplication of physical values.
For every \(k\ge1\),
\[
 A_2^k=S^{-1}\mathsf P^{-1}\mathbf H_N
                 (\mathsf B_N\mathbf H_N)^{k-1}\mathsf D.
 \tag{24}
\]
An adjacent arbitrary signed power retains its own crossing:
\[
 A_2A_n
    =S^{-1}\mathsf P^{-1}\mathbf H_N\mathsf B_N
                       \mathbf H_N\mathsf D M^{n-2},
 \qquad n\in\mathbb Z.
 \tag{25}
\]
These are exact finite identities, with all turns and all original
crossing powers inside their specified matrices.

For example the actually observed two-block sum, with any original
right coefficient column \(b\), is
\[
 \ell^TA_2^2b
  =\sum_{i,j,k,l=0}^{D}
      \frac{(\ell^TS^{-1})_i}{P_i}
          H_N(i/N,j/N)(\mathsf B_N)_{jk}
          H_N(k/N,l/N)(\mathsf D b)_l.
 \tag{26}
\]
Putting \(b=v(w)\), and differentiating that original Newton column,
retains every specified ordinary boundary normal. At a branching
vertex the original multiplication tensor is inserted in those
coefficient slots, as in
[arbitrary-power compilation](research_arbitrary_power_source_compilation.md).
Multilinearity permits (22) slotwise; it does not replace that tensor
by a product of node values. Uncontracted ordinary variables remain
unreduced, exactly as in the source compiler.

Since every matrix outside \(\mathbf H_N\) in (22) is invertible,
the full homogeneous node matrix is invertible. Thus any nonzero
incoming row in (17) produces a finite function not identically zero.
A specified final closing functional can still cancel it. Neither
invertibility nor (13) supplies its large-\(N\) lower bound.

The extension in Proposition 1 removes the incomplete-node obstacle
to using the homogeneous period in actual adjacent compositions.
The remaining analytic problem is the signed sum (20) or (26),
with its genuine prefix, interface, and final observation. The local
critical contribution to one period, or the disappearance of the
particular term at nodes, does not alone estimate that complete sum.
