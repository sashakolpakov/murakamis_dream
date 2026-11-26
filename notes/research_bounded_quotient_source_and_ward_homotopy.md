# A bounded quotient source and its marked Ward homotopy

Private written proof, 19 November 2026.

The actual pointed source on total intertwiners has a quotient
representative whose regularized operator norm is bounded independently
of the level. It is obtained from an explicit orthogonal complement at
the root and the actual holomorphic Cartan frame. Its residue and finite
part have norms at most \(1/m\) and \(1+(m-1)(N-1)\).

For arbitrary analytic marks the replacement has an exact correction
by the original total \(E\)- and \(F\)-commutators. Both correction
matrices are explicit and have controlled exponential bounds. The
polynomial bound on the quotient coupon does not turn those bounds
into polynomial bounds, or make the source positive.

The complete directs F, M, and C are pinned below. F supplies the
forced source and its capped partial inverse; M supplies the actual
meridian frames; C bounds the specified grouped \(E\)-primitive.
The new quotient section, coupon, marked comparison, and root
normal packet are proved here.

## 1. Physical spaces and the exact quotient

Fix \(m\ge2\), \(r=m-1\), \(N\ge2\), \(d=N-1\), and
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad M=e^\mu,\quad x=-M/q.
 \tag{1}
\]
The physical occupation coefficient basis on
\(V=(\mathbb C^N)^{\otimes m}\) is declared orthonormal.
All operator and adjoint symbols in this note use that Euclidean
metric. Set \(U=(\mathbb C^N)^{\otimes r}\).
The first-head insertion and extraction are \(i_0,p_0\), and
\[
 q_F(M)=p_0S(M)^{-1},\qquad
 q_Fi_0=I,\qquad \ker q_F=\operatorname{im}F_\Sigma(M).
 \tag{2}
\]
These are F's actual finite prefix maps, not an asymptotic quotient.
They preserve total integer occupation, with the first occupation
omitted on \(U\). Write \(J_iw_a=aw_a\) and \(J=\sum_iJ_i\).

The original highest-cut source for every analytic full matrix is
\[
 \Phi(A)=\operatorname{Tr}_V((P_0\otimes g)A),\qquad
 P_0=|0\rangle\langle0|,\quad
 g=K_{\rm r}^{-d}=M^{-rd}g_0 .
 \tag{3}
\]
Every prescribed scalar crossing, zero-framing, dimension, or
peripheral line remains in \(A\), or is explicitly multiplied into
the entire equality below.

M's whole-meridian frame is
\[
 B_F(M)=M^{-\sum_{i=1}^m(i-1)J_i}=e^{\mu G},
 \quad G=-\sum_{i=1}^m(i-1)J_i,\quad
 B_{\rm t}(M)=M^{-\sum_{i=2}^m(i-1)J_i},
 \tag{4}
\]
\[
 F_\Sigma(M)=B_FF_\Sigma(1)B_F^{-1},\qquad
 q_F(M)=B_{\rm t}q_0B_F^{-1},\quad q_0=q_F(1).
 \tag{5}
\]
All of these identities retain the bottom and top physical caps.

## 2. An explicit bounded section and a holomorphic projector

Because \(q_0i_0=I\) and \(i_0\) is isometric,
\[
 \mathcal G_0=q_0q_0^*\ge I_U.
 \tag{6}
\]
Equivalently, the first block of \(q_0\) is \(I_U\), so its Gram
matrix is \(I_U\) plus a sum of positive matrices. Define
\[
 j_\perp=q_0^*\mathcal G_0^{-1},\qquad
 P_\perp=j_\perp q_0.
 \tag{7}
\]
Then
\[
 q_0j_\perp=I,\qquad
 P_\perp=P_\perp^*=P_\perp^2,\qquad
 \ker P_\perp=\operatorname{im}F_\Sigma(1),
 \quad \|j_\perp\|\le1,\quad \|P_\perp\|=1.
 \tag{8}
\]
Indeed \(j_\perp^*j_\perp=\mathcal G_0^{-1}\le I\); the other
claims follow directly from (6)--(7). This uses no unknown
singular-value gap for the tensor operator \(F_\Sigma\).
Both \(\mathcal G_0\) and (7) preserve their integer-degree blocks.

Transport these fixed root matrices by the actual frame:
\[
 j(M)=B_F(M)j_\perp B_{\rm t}(M)^{-1},\qquad
 P(M)=B_F(M)P_\perp B_F(M)^{-1}.
 \tag{9}
\]
Equations (5),(8) give
\[
 q_Fj=I,\quad jq_F=P,\quad P^2=P,\quad
 \ker P=\operatorname{im}F_\Sigma(M).
 \tag{10}
\]
Thus \(j\) is a holomorphic section of the original quotient
coordinates, and \(P\) is a holomorphic projector. It preserves
\(J\), hence commutes with the actual total Cartan \(K_\Sigma(M)\).
The projector is generally oblique away from \(\mu=0\).

The change back to the original section is exactly square-zero.
Put \(P_{\rm h}=i_0q_F\) and \(\mathcal N=P_{\rm h}-P\).
Both projectors have kernel \(\operatorname{im}F_\Sigma\), and
\(q_F\mathcal N=0\). Therefore
\[
 \mathcal N^2=0,\quad P\mathcal N=0,\quad\mathcal NP=\mathcal N,
 \quad
 \mathscr U=I+\mathcal N,\quad\mathscr U^{-1}=I-\mathcal N,
 \tag{10a}
\]
\[
             q_F\mathscr U=q_F,\qquad
             \mathscr Uj=i_0,\qquad
             \mathscr UP\mathscr U^{-1}=P_{\rm h}.
 \tag{10b}
\]
More generally, for any sections \(j_i\) of this same \(q_F\),
\(\mathcal N_{ij}=(j_j-j_i)q_F\) satisfy
\(\mathcal N_{ij}\mathcal N_{kl}=0\) and
\(\mathcal N_{ij}+\mathcal N_{jk}=\mathcal N_{ik}\).
These identities follow from \(q_F(j_j-j_i)=0\).
Thus their section transitions compose additively, without an
omitted higher correction. This algebraic nilpotence does not bound
the norms of the transitions or identify geometric relative cycles.

For fixed \(0<\eta<\pi/m\), on the disk \(|N\mu|\le\eta\),
the matrices \(B_F^{\pm1},B_{\rm t}^{\pm1}\) have bounded norms
depending only on \(m,\eta\). In particular
\[
 \|P(M)\|\le e^{\eta mr},\qquad
                    \|j(M)\|\le C_{m,\eta}.
 \tag{11}
\]
All fixed true \(\mu\)-derivatives have polynomial cost by the
same explicit diagonal formulas or a buffered Cauchy estimate.

For comparison, at each fixed complex \(M\) the Euclidean orthogonal
projector onto \((\operatorname{im}F_\Sigma(M))^\perp\) is
\[
 P_F^{\rm orth}(M)=q_F(M)^*
           [q_F(M)q_F(M)^*]^{-1}q_F(M).
 \tag{12}
\]
It has norm one and preserves degree. Its dependence on complex
\(\mu\) is not holomorphic. We use (9), rather than differentiating
(12), in every meridian-normal formula.

## 3. The bounded quotient coupon and the unmarked source

Define
\[
 H_{\rm tot}(M)=D_N(-qK_\Sigma(M)),\qquad
 H(M)=D_N(MK_{\rm r}(M)),\qquad
 D_N(z)=\frac{z^N-z^{-N}}{z-z^{-1}}.
 \tag{13}
\]
The Laurent-polynomial continuation defines \(D_N\) at \(\pm1\).
On total integer degree \(a\),
\[
 -qK_\Sigma(M)=M^m\widetilde K_0,\qquad
 \widetilde K_0=(-qK_\Sigma(1)),\qquad
 \widetilde K_0|_{J=a}=(-q^{-1})^rQ^{-a}.
 \tag{14}
\]
Therefore \(\widetilde K_0^N=\varepsilon I\), where
\(\varepsilon=(-1)^{(N+1)r}\). The same degree on \(U\) has
\(MK_{\rm r}(M)=M^m(-q^{-1})^rQ^{-a}\). Consequently
\[
 q_FH_{\rm tot}=Hq_F,\qquad
 H_{\rm tot}i_0=i_0H,\qquad H_{\rm tot}j=jH.
 \tag{15}
\]
The last identity uses the exact degree preservation of \(j\).

On the punctured disk where the displayed inverses exist, set
\[
 \boxed{\quad
 Q_{\rm b}(M)=D_N(M)H_{\rm tot}(M)^{-1}P(M)
            =D_N(M)j(M)H(M)^{-1}q_F(M).
 \quad}\tag{16}
\]
Every identity extends meromorphically to the root. Since \(P\)
commutes with \(H_{\rm tot}\), inserting \(P\) also on the left
of (16) gives the same matrix.

Let \(W(M)\) be an analytic total intertwiner. It preserves
\(\operatorname{im}F_\Sigma\), so its induced quotient is the
actual matrix
\[
 B(W)=q_FW i_0,\qquad q_FW=B(W)q_F.
 \tag{17}
\]
It follows that \(q_FWj=B(W)\). Rectangular trace, followed by
F's homogeneous source formula, proves
\[
 \boxed{\quad
 \operatorname{Tr}_V(Q_{\rm b}W)
    =D_N(M)\operatorname{Tr}_U(H^{-1}B(W))
    =\Phi(W).
 \quad}\tag{18}
\]
This is the original pointed source, not a new normalized trace.
The same proof, using the least-norm section at that \(M\), gives
the pointwise orthogonal version
\[
 \Phi(W)=\operatorname{Tr}
 \bigl(D_N(M)P_F^{\rm orth}H_{\rm tot}^{-1}
                            P_F^{\rm orth}W\bigr).
 \tag{19}
\]
Equation (19) is not used as a holomorphic family.

The norm in (16) is genuinely bounded after regularization.
For \(u=N\mu\), each physical \(\widetilde K_0=\chi\), \(|\chi|=1\),
has
\[
 \mu D_N(M)H_{\rm tot}^{-1}
  =\frac{u/N}{\sinh(u/N)}
      \frac{\sinh u}{2\varepsilon\sinh(m u)}
        (e^{m u/N}\chi-e^{-m u/N}\chi^{-1}).
 \tag{20}
\]
This is uniformly bounded and holomorphic, with removable value at
zero, on every closed disk \(|u|\le\eta<\pi/m\). Combining it with
(11) proves
\[
 \boxed{\quad
             \sup_{|N\mu|\le\eta}\|\mu Q_{\rm b}(e^\mu)\|
                  \le C_{m,\eta}.
 \quad}\tag{21}
\]
There is no level-dependent exponential or polynomial in this bound.
The matrix has rank at most \(N^r\); its trace norm is bounded by
\(C_{m,\eta}N^r\) after the same regularization.

For \(\eta<\eta'<\pi/m\), buffered Cauchy estimates give
\[
 \sup_{|N\mu|\le\eta}
    \|\partial_\mu^k[\mu Q_{\rm b}(e^\mu)]\|
                   \le C_kN^k,\qquad k\ge0\ \text{fixed}.
 \tag{22}
\]
Thus all the true source-normal data of this coupon have polynomial
cost. The adjoint in (7) was taken only at the fixed root; it creates
no antiholomorphic meridian dependence in (22).

## 4. Explicit residue, finite part, and the original root value

Write
\[
 Q_{\rm b}(e^\mu)=\mu^{-1}R_{\rm b}+C_{\rm b}
                                      +\mu Q_{{\rm b},1}+\cdots .
 \tag{23}
\]
Expansion of the actual diagonal factor in (20), and
\(P'(0)=[G,P_\perp]\), gives
\[
 \boxed{\begin{split}
 R_{\rm b}&=\frac{\widetilde K_0-\widetilde K_0^{-1}}
                            {2\varepsilon m}P_\perp,\\
 C_{\rm b}&=\frac{\widetilde K_0+\widetilde K_0^{-1}}
                            {2\varepsilon}P_\perp
       +\frac{\widetilde K_0-\widetilde K_0^{-1}}
                            {2\varepsilon m}[G,P_\perp].
 \end{split}}\tag{24}
\]
The diagonal factors commute with \(P_\perp\) and \(G\) because
they are scalar on total integer degree. In particular
\[
       \|R_{\rm b}\|\le1/m,\qquad
       \|C_{\rm b}\|\le1+rd,\qquad
       \|Q_{{\rm b},j}\|\le C_jN^{j+1}\quad(j\ge-1).
 \tag{25}
\]
For the middle inequality use
\(\|G\|=mrd/2\) and \(\|[G,P_\perp]\|\le2\|G\|\).
The general coefficient estimate follows from (22).

For an analytic total intertwiner
\(W=W_0+\mu W_1+\mu^2W_2+\cdots\), the original left side of (18)
is analytic. Its residue therefore gives the exact cancellation
\[
                         \operatorname{Tr}(R_{\rm b}W_0)=0.
 \tag{26}
\]
Its value is the explicit original-root row
\[
 \boxed{\quad
 \operatorname{Tr}((P_0\otimes g_0)W_0)
       =\operatorname{Tr}(C_{\rm b}W_0+R_{\rm b}W_1).
 \quad}\tag{27}
\]
This retains the true first meridian derivative of the word.
The next coefficient is likewise
\[
 \operatorname{Tr}((P_0\otimes g_0)(W_1-rdW_0))
  =\operatorname{Tr}(Q_{{\rm b},1}W_0+C_{\rm b}W_1+R_{\rm b}W_2).
 \tag{28}
\]
Here \(W_2\) is the Taylor coefficient, one half the second derivative.
The pivot derivative and the additional jet in (28) are explicit.
All crossing and external scalar derivatives are those of the
original \(W(M)\).

## 5. The exact marked correction uses the original arrows

For an arbitrary analytic matrix \(A(M)\), (18) need not hold.
Retain F's actual source coupon and partial inverse
\[
 P_{\rm h}=i_0q_F,\qquad
 Q_{\rm h}=D_N(M)i_0H^{-1}q_F
          =D_N(M)H_{\rm tot}^{-1}P_{\rm h},
 \tag{29}
\]
\[
 \lambda_Fw_a=
 \begin{cases}(1-Q^a)^{-1}w_{a-1},&a>0,\\0,&a=0,\end{cases}
 \qquad
 \Lambda_F=S(\lambda_F\otimes I)S^{-1},\qquad
 F_\Sigma\Lambda_F=I-P_{\rm h}.
 \tag{30}
\]
The two projectors \(P_{\rm h}\) and \(P\) have exactly the same
kernel, \(\operatorname{im}F_\Sigma\), and \(q_FP_{\rm h}=q_FP=q_F\).
Hence \(P_{\rm h}-P\) kills this image and has its range inside it.
The same is true of
\[
             \mathcal D=Q_{\rm h}-Q_{\rm b},
 \tag{31}
\]
because \(H_{\rm tot}^{-1}\) is scalar on each integer degree, and
\(\operatorname{im}F_\Sigma\) is graded. In particular
\(\mathcal DF_\Sigma=0\) and \(P_{\rm h}\mathcal D=0\).
Define the explicit meromorphic matrix
\[
                        \mathcal V_F=-\Lambda_F\mathcal D .
 \tag{32}
\]
Then \(\mathcal V_FF_\Sigma=0\) and
\(F_\Sigma\mathcal V_F=-\mathcal D\). Thus
\[
                     [\mathcal V_F,F_\Sigma]=Q_{\rm h}-Q_{\rm b}.
 \tag{33}
\]

F gives \(P_0\otimes g-Q_{\rm h}=[\mathcal W_E,E_\Sigma]\)
for its specified grouped primitive. Combining it with (33) proves
the full matrix and marked scalar identities
\[
 \boxed{\begin{split}
 P_0\otimes g-Q_{\rm b}
      &=[\mathcal W_E,E_\Sigma]+[\mathcal V_F,F_\Sigma],\\
 \Phi(A)&=\operatorname{Tr}(Q_{\rm b}A)
    +\operatorname{Tr}(\mathcal W_E[E_\Sigma,A])
    +\operatorname{Tr}(\mathcal V_F[F_\Sigma,A]).
 \end{split}}\tag{34}
\]
The trace sign follows from
\(\operatorname{Tr}([X,G]A)=\operatorname{Tr}(X[G,A])\).
These are the original total arrows. No arbitrary functional
annihilating the commutant has been substituted for a Ward current.

All three coupons in (34) have at most a simple pole.
For example, put \(Y_E=[E_\Sigma,A]\), \(Y_F=[F_\Sigma,A]\), and
\[
 \mathcal W_E=\mu^{-1}E_{-1}+E_0+\cdots,\qquad
 \mathcal V_F=\mu^{-1}F_{-1}+F_0+\cdots .
 \]
Analyticity of the original source gives
\[
 0=\operatorname{Tr}(R_{\rm b}A_0+
                              E_{-1}Y_{E,0}+F_{-1}Y_{F,0}),
 \tag{35}
\]
\[
 \Phi(A)(0)=\operatorname{Tr}\bigl(
 C_{\rm b}A_0+R_{\rm b}A_1+
 E_{-1}Y_{E,1}+E_0Y_{E,0}+
 F_{-1}Y_{F,1}+F_0Y_{F,0}\bigr).
 \tag{36}
\]
Both current normals include the derivative of the actual total
arrow as well as the derivative of \(A\). Equations (35)--(36)
do not discard separate residues. Multiplying by a prescribed
analytic scalar line differentiates that line in each unresolved
term; those residue contributions cancel only in the complete
identity (35).
A prescribed meromorphic outside line instead retains its full
Laurent multiplication; it is not covered by an analytic-line
finite-part shortcut.

## 6. Quantitative scope of the two homotopies

C proves in this same coefficient Euclidean norm that, on the
buffered collar,
\[
 \|S(M)^{\pm1}\|\le C2^{rN},\qquad
 \|\mu Q_{\rm h}(M)\|\le C2^{rN},\qquad
 \|\mu\mathcal W_E(M)\|\le CN^p2^{(5m-2)N}.
 \tag{37}
\]
Also \(\|\lambda_F\|\le N/4\), since
\(|1-Q^a|\ge4\min(a,N-a)/N\). Combining (21),(30)--(32),(37)
gives the actual additional homotopy bound
\[
 \boxed{\quad
           \|\mu\mathcal V_F(M)\|\le C N\,2^{3rN}.
 \quad}\tag{38}
\]
Every fixed true \(\mu\)-derivative of the two regularized
homotopies has the corresponding extra polynomial power of \(N\).
Their Laurent coefficient of order \(j\ge-1\) has an additional
factor \(N^{j+1}\), by buffered Cauchy estimates.

Thus the coupon (16) has polynomial normal data, while the proved
comparison of arbitrary marks in (34) has exponential costs (37)--(38).
No polynomial tensor Hodge gap is asserted. The bounded inverse in
(6) concerns the quotient map \(q_0\), whose first block is \(I\);
it is not a polynomial bound for a right inverse of \(F_\Sigma\)
or for a joint \(E,F\) commutator solver.

These bounds cover all physical occupations, all levels \(N\ge2\),
and every fixed head count. They do not use a small-occupation
restriction. They do not turn a locally bounded coherent symbol
into a matrix norm or bound a closed geometric current without
its remaining contraction. The reciprocal Cartan weights in (20)
remain, so the construction is not a positive-norm formula.
No nonzero geometric contribution or original-source lower bound
is inferred.

## Complete proof directs

* F: notes/research_forced_source_and_opposite_kernel_transport.md,
  SHA256 2e92bab4e3c510519098e3a10ed4227a8f4b492393b3742d02e4fdcaa3cca0f5.
* M: notes/research_actual_meridian_source_frames.md,
  SHA256 6f58fba195ba5e8208e1d5180a1d684b933f9f5d50eb28efc56609580fe29976.
* C: notes/research_grouped_ward_cosource_collar_bound.md,
  SHA256 df2a46cd10570131c9040556636fc88c151afe308ab8d0198e3e163433287bf8.

All three complete matching directs were freshly wholly read
nontruncated in this uninterrupted author/review sequence. Every
used implication, source order, and meridian normalization was
checked. Only written mathematics and text/hash operations were
used; frozen and public files were not edited.
