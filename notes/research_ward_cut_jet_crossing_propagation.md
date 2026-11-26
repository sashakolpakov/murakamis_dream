# Exact Ward cut-jet propagation under original crossings

Private written proof, 17 November 2026.

The two polynomial channels of the original Ward representative
give a positive norm on the full finite source, including its
physical first normals. Their connection is polynomially bounded
in the level. In these coordinates every integer multiplication
crossing is an exact quadratic-phase unitary on the value channel,
with an explicit commutator and normal shear on the other channel.
Both the crossing and its inverse have polynomial operator bounds.

Positive full-Hermite norms and finite Fourier value problems are
already available. The point here is the positive measure on the
actual Ward cut, a uniform bound for its normal connection, and
the resulting exact coherent two-channel crossing formula.
The original closing is recovered explicitly. No turn estimate,
geometric action bound, or scalar lower bound is asserted.

## 1. Original source and the two polynomial channels

Put
\[
 N\ge2,\quad D=N-1,\quad m=\lfloor N/2\rfloor,\quad
 \theta=\pi/N,\quad q=e^{i\theta},\quad
 \eta=(-1)^D,\quad \kappa=q^{D^2/2},
\]
\[
 \theta_j=(2j+1)\theta,\quad c_j=2\cos\theta_j,\quad
 a_j=4-c_j^2,\quad
 P_N(C)=2T_N(C/2)+2,\quad
 \mathcal A_N=\mathbb C[C]/(P_N).
 \tag{1}
\]
The double indices are \(0\le j<m\). At odd \(N=2m+1\)
there is also the simple node \(c_*=-2\), with no normal.
Use the original Newton kernel and rows
\[
 s_r=2\sin(r\theta),\quad S_r=\prod_{b=1}^rs_b,\quad
 e_r(C)=S_r^{-2}\prod_{b<r}(c_b-C),\quad
 K_N(w,C)=\sum_{r=0}^De_r(w)e_r(C),
\]
\[
 F_j=K_N(c_j,\cdot),\qquad G_j=\partial_wK_N(c_j,\cdot),
 \qquad Te_r=e_{D-r},\qquad
 \phi_N(A)=\eta N^2[C^D]\operatorname{can}(A).
 \tag{2}
\]
All products, derivatives at physical nodes and crossings below
belong to this full quotient. In particular its normal data are
not replaced by a distinct-value algebra.

The positive Ward-measure theorem supplies
\[
 d\mu_N(x)=\frac{N^2\rho_N(x)}{P_N(x)}\,dx,\qquad
 \rho_N(x)=\frac{N}{4\pi\sin\theta}
       \tanh\!\left(\frac N2\operatorname{arcosh}(x/2)\right),
 \quad x>2,
\]
\[
 \langle F_j,F_k\rangle_{\mu_N}=h_j\delta_{jk},
 \qquad h_j=\frac1{4\sin\theta\sin\theta_j}.
 \tag{3}
\]
Here \(\langle f,g\rangle=\int\overline f g\,d\mu_N\).
Write \(\mathcal P_m=\{f:\deg f<m\}\) with this Hilbert
norm and \(f_j=F_j/\sqrt{h_j}\). Every double row has degree
\(j\); its roots are simple and lie in \((2,\infty)\).
At odd levels \(F_*\) has degree \(m\) and infinite squared
cut norm. Its original simple value will be a separate coordinate.

Let \(Q=\widetilde Q_N\) be the exact even Ward representative
of \(G_0\) on \(\Omega=\mathbb C\setminus[2,\infty)\).
Retain the common-shift determinant
\[
 F_j^\epsilon(C)=
 \frac{\det(\mathcal J_j(\epsilon)-CI)}
             {\prod_{r<j}A(r+\epsilon)},\qquad
 R_j=\left.\partial_\epsilon F_j^\epsilon\right|_0,\qquad
 R_0=0,
\]
\[
 c'(j)=-4\theta\sin\theta_j,\qquad
 b_j=\frac{c'(0)}{c'(j)}=\frac{\sin\theta}{\sin\theta_j},
 \qquad Z_j=\frac{R_j}{c'(0)}.
 \tag{4}
\]
The constant \(c_0\) in \(\mathcal J_j(\epsilon)\) is held
fixed. The pinned source theorem gives the exact full-jet
representative
\[
             \widehat G_j=b_j(QF_j+Z_j).
 \tag{5}
\]
The degree of \(Z_j\) is at most \(j\). Define the real
degree-preserving connection
\[
                    \mathscr D_NF_j=Z_j.
 \tag{6}
\]
At \(N=2\) this is the zero operator on constants.

For any actual \(A\in\mathcal A_N\), the source-equivalent
representative of \(TA\) is
\[
 \widehat H_A=Y_A+QL_A,\qquad
 L_A=\eta\sum_{j<m}\frac{A(c_j)}{h_j}F_j,
\]
\[
 Y_A=\eta\sum_{j<m}
 \left\{\frac{a_jA(c_j)}{c'(j)}R_j
             +(a_jA'(c_j)-c_jA(c_j))F_j\right\}
       +\mathbf1_{\mathrm{odd}}s_AF_*,
 \qquad s_A=A(-2).
 \tag{7}
\]
The \(s_A\) coordinate is used only at odd levels. Set
\[
 Y_A^0=Y_A-\mathbf1_{\mathrm{odd}}s_AF_*,
 \qquad
 J_A=\eta\sum_{j<m}(a_jA'(c_j)-c_jA(c_j))F_j.
\]
Since \(a_jb_j=1/h_j\), these identities give
\[
              Y_A^0=\mathscr D_NL_A+J_A,
              \qquad Y_A^0,L_A,J_A\in\mathcal P_m.
 \tag{8}
\]

This is also an exact common-shift jet. With
\(c(z)=2\cos((2z+1)\theta)\), define, for sufficiently small
\(\epsilon\) at each fixed level,
\[
 L_{A,\epsilon}(C)=4\eta\sin\theta
    \sum_{j<m}\sin(\theta_j+2\theta\epsilon)
                   A(c(j+\epsilon))F_j^\epsilon(C).
\]
Direct differentiation, including the derivative of the sine
weight, gives
\[
 Y_A^0=-\frac1{4\theta\sin\theta}
                \left.\partial_\epsilon L_{A,\epsilon}\right|_0.
 \tag{9}
\]
This common shift is the determinant deformation in (4).
It is not a global degree translation or a Poisson formula,
and no level-independent complex \(\epsilon\) domain is needed.

## 2. Uniform logarithmic moments on the actual cut

**Lemma 1.** There is an absolute constant \(C\) such that
for every \(N\ge2\) and double row \(j\),
\[
          \int_2^\infty(1+\log x)|f_j(x)|^2\,d\mu_N(x)
                         \le C(1+\log N).
 \tag{10}
\]

**Proof.** The finite Jacobi determinant for \(F_j\) has
diagonal \(c_0+A_r+C_r\) and off-diagonal
\(-\sqrt{A_rC_{r+1}}\), where
\[
 A_r=\frac{s_{r+1}^4}{s_{2r+1}s_{2r+2}},\qquad
 C_r=\frac{s_r^4}{s_{2r}s_{2r+1}},\qquad C_0=0.
 \tag{11}
\]
Only the original pre-fold range is used. Every nonzero
denominator factor in the matrices for the double rows
has index between \(1\) and \(N-1\), and hence is at least
\(4/N\). Thus \(A_r,C_r\le N^2\). The row-sum bound for
these real symmetric matrices gives
\[
                   2<\lambda_{j,k}\le6N^2
 \tag{12}
\]
for every root of \(F_j\). The lower assertion also follows
from (3); only the upper bound is needed now. For the
degree-zero row there is no root to bound.

Choose \(R_N=16N^3\). For \(x\ge R_N\), factoring the
roots in (12) gives, with absolute comparison constants,
\[
 |F_j(x)|^2\asymp |\operatorname{lc}F_j|^2x^{2j},
 \qquad P_N(x)\asymp x^N,\qquad N^2\rho_N(x)\asymp N^4.
 \tag{13}
\]
For the first comparison, each \(\lambda_{j,k}/x\le3/(8N)\)
and their sum is bounded; apply
\(-2u\le\log(1-u)\le-u\) for \(0\le u\le1/2\).
For the second, all \(N\) roots counted with multiplicity
lie in \([-2,2]\), and the same product estimate applies.
For the third, \(2/N\le\sin\theta\le\pi/N\) and the
hyperbolic tangent is bounded below by an absolute positive
constant on this tail.

Write \(a=N-2j\). In the entire double range \(a\ge2\).
The elementary tail integrals satisfy
\[
 \frac{\int_{R_N}^\infty(\log x)x^{-a}\,dx}
      {\int_{R_N}^\infty x^{-a}\,dx}
                  =\log R_N+\frac1{a-1}\le\log R_N+1.
 \tag{14}
\]
Combining both directions of (13) shows that the logarithmic
tail moment of \(|F_j|^2\) is at most
\(C(\log R_N+1)\) times its tail mass, hence at most that
constant times \(h_j\). On \(2<x<R_N\), use
\(\log x\le\log R_N\) and (3).
This proves (10), including \(N=2\).

In particular no first moment of \(|F_j|^2d\mu_N\) has
been invoked. That first moment diverges for the last
double row at even levels; its logarithmic moment still
satisfies (10). \(\square\)

Let \(Q_{\mathrm R}(x)=(Q_+(x)+Q_-(x))/2\), a real function.
The exact cotangent formula is
\[
 Q(-2\cos t)=-
 \frac{g_N'(D/2-t/(2\theta))-g_N'(0)}
                         {2\theta\sin\theta},\qquad
 g_N'(z)=\frac{\pi}{N^2}
       \sum_{r=0}^D(z-r)\cot\frac{\pi(z-r)}N .
 \tag{15}
\]
It implies
\[
 |Q_{\mathrm R}(x)|
            \le CN^2(1+\log N+\log x),\qquad x>2.
 \tag{16}
\]
Indeed write \(x=2\cosh h\). For \(0\le h\le1\), the
pinned fixed-height Ward bound at \(t=\pi+ih\) is
\(CN^2(1+\log N)\), on both cut banks.
For \(h\ge1\), every cotangent in (15) has imaginary
argument part \(-h/2\), and its modulus is at most
\(\coth(h/2)\). The finite sum then gives
\(|g_N'(D/2-t/(2\theta))|\le C(1+h)\).
At \(z=0\), the removable \(r=0\) term is \(1/N\);
bounding the others by
\(C N/\min(r,N-r)\) before summing gives
\(|g_N'(0)|\le C(1+\log N)\).
Finally \(\theta\sin\theta\asymp N^{-2}\) and
\(h\le\log x\). This proves (16).

## 3. The connection Gram identity and its polynomial bound

**Theorem 2.** In the orthonormal basis \(f_j\), let
\[
 (M_N)_{kj}=\int_2^\infty Q_{\mathrm R}(x)f_k(x)f_j(x)
                                                    \,d\mu_N(x).
\]
Then the connection in (6) is real upper triangular and
\[
 \boxed{\quad
 \mathscr D_N+\mathscr D_N^*
              =\operatorname{diag}(c_jh_j)-2M_N,\qquad
 \|\mathscr D_N\|\le CN^3(1+\log N).
 \quad}
 \tag{17}
\]
The matrix \(M_N\) is defined by these finite form integrals.
No boundedness of multiplication by \(Q_{\mathrm R}\)
on the whole cut Hilbert space is being asserted.

**Proof.** The exact original Gram entry is
\(\phi_N(G_jG_k)=\eta c_j a_j^{-2}\delta_{jk}\).
Use the whole keyhole for
\(\widehat G_j\widehat G_k/P_N\). The physical residues
are unchanged by full-jet equivalence. Since
\(j+k\le2m-2\le N-2\), the outer circle tends to zero,
also with the two logarithmic factors from \(Q^2\).
The small endpoint cap tends to zero as well.
Its upper-minus-lower jump and (5) give exactly
\[
 \int_2^\infty
     (Z_jF_k+F_jZ_k+2Q_{\mathrm R}F_jF_k)\,d\mu_N
                           =c_jh_j^2\delta_{jk}.
 \tag{18}
\]
Here \(a_jb_j=1/h_j\) accounts for the normalization.
Every integral is absolutely convergent by (10) and (16).
Dividing by \(\sqrt{h_jh_k}\) proves the first identity
of (17). Degree preservation and real coefficients make
\(\mathscr D_N\) real upper triangular. Thus (17)
determines all its entries: above the diagonal they are
\(-2(M_N)_{kj}\), and on the diagonal they are
\(c_jh_j/2-(M_N)_{jj}\).

By (10), (16), and Cauchy--Schwarz with weight
\(1+\log N+\log x\),
\[
                   |(M_N)_{kj}|\le CN^2(1+\log N).
 \tag{19}
\]
Also \(|c_jh_j|\le CN^2\), since
\(\sin\theta_j\ge\sin\theta\) in the double range.
There are at most \(m^2\) entries. The Frobenius matrix
norm consequently bounds the operator norm by
\(CmN^2(1+\log N)\), proving the second part of (17).
For \(N=2\), \(Z_0=0\) directly; the same keyhole and
bounds remain valid. \(\square\)

## 4. Exact crossing of the full Ward jet

The original crossing data, with their scalar retained, are
\[
 \nu_j=(-1)^jq^{j(j+1)},\quad
 r_{p,j}=R(c_j)^p=\kappa^p\nu_j^p,\quad
 \alpha_j=\frac{R'(c_j)}{R(c_j)}
                  =\frac{i(D-2j)}{4\sin\theta_j}.
 \tag{20}
\]
For each integer \(p\), define the unitary and skew-adjoint
diagonal operators on \(\mathcal P_m\)
\[
 \mathscr U_pF_j=r_{p,j}F_j,\qquad
 \mathscr VF_j=v_jF_j,\qquad
 v_j=a_j\alpha_jh_j=\frac{i(D-2j)}{4\sin\theta}.
 \tag{21}
\]
In particular \(\|\mathscr V\|\le CN^2\).
The unitary has the exact coherent integral formula
\[
 (\mathscr U_pf)(C)=\int_2^\infty
    \left\{\sum_{j<m}\frac{r_{p,j}F_j(C)F_j(x)}{h_j}\right\}
                                      f(x)\,d\mu_N(x),
                 \qquad f\in\mathcal P_m .
 \tag{22}
\]
Every discrete quadratic phase is present in this finite sum.

**Theorem 3.** For every actual \(A\in\mathcal A_N\) and
integer \(p\), multiplication by the original \(R^p\)
acts on its two polynomial channels by
\[
 \boxed{\quad
 \begin{pmatrix}Y_{R^pA}^0\\L_{R^pA}\end{pmatrix}
 =
 \begin{pmatrix}
 \mathscr U_p&
 [\mathscr D_N,\mathscr U_p]+p\mathscr U_p\mathscr V\\
 0&\mathscr U_p
 \end{pmatrix}
 \begin{pmatrix}Y_A^0\\L_A\end{pmatrix}.
 \quad}
 \tag{23}
\]
At odd levels the separate coordinate is
\[
                      s_{R^pA}=R(-2)^p s_A.
 \tag{24}
\]
Its multiplier has modulus one and there is no additional
simple-node normal.

**Proof.** The physical product rule gives
\[
 (R^pA)(c_j)=r_{p,j}A(c_j),\qquad
 (R^pA)'(c_j)=r_{p,j}\{A'(c_j)+p\alpha_jA(c_j)\}.
 \tag{25}
\]
Equations (7)--(8) therefore imply
\[
 L_{R^pA}=\mathscr U_pL_A,\qquad
 J_{R^pA}=\mathscr U_pJ_A+p\mathscr U_p\mathscr VL_A.
 \tag{26}
\]
Substitute \(J_A=Y_A^0-\mathscr D_NL_A\) to obtain
(23). The simple value gives (24).
The same proof works for negative powers, since the
original crossing is a unit of the full quotient.
These matrices obey the group law for integer powers;
their inverse is the matrix for \(-p\).
No next ordinary fold row or boundary wrap is used.
\(\square\)

## 5. A positive norm on the entire original source

Define
\[
 \|A\|_{\mathrm{cut}}^2
       =\|Y_A^0\|_{\mu_N}^2+\|L_A\|_{\mu_N}^2
                            +\mathbf1_{\mathrm{odd}}|s_A|^2,
\]
\[
 \|A\|_{\mathrm{cov}}^2
       =\|J_A\|_{\mu_N}^2+\|L_A\|_{\mu_N}^2
                            +\mathbf1_{\mathrm{odd}}|s_A|^2.
 \tag{27}
\]
Both are positive definite on the full \(N\)-dimensional
space \(\mathcal A_N\), not on a quotient. More explicitly,
\[
 \|A\|_{\mathrm{cov}}^2
  =\sum_{j<m}\left\{
      \frac{|A(c_j)|^2}{h_j}
       +h_j|a_jA'(c_j)-c_jA(c_j)|^2\right\}
       +\mathbf1_{\mathrm{odd}}|A(-2)|^2.
 \tag{28}
\]
To recover the actual data, expand
\[
 L_A=\sum\ell_jF_j,\qquad
 Y_A^0-\mathscr D_NL_A=\sum z_jF_j.
\]
Then
\[
       A(c_j)=\eta h_j\ell_j,\qquad
       A'(c_j)=\frac{\eta z_j+c_jA(c_j)}{a_j}.
 \tag{29}
\]
Together with the odd value these are exactly all physical
Hermite data; their unique canonical interpolant recovers
\(A\). Conversely every such pair and odd value is allowed.
The triangular change (8) and its inverse give
\[
 (1+\|\mathscr D_N\|)^{-1}\|A\|_{\mathrm{cov}}
 \le\|A\|_{\mathrm{cut}}
 \le(1+\|\mathscr D_N\|)\|A\|_{\mathrm{cov}}.
 \tag{30}
\]

It follows from (23) that, with an absolute constant,
\[
 \boxed{\quad
 \|R^pA\|_{\mathrm{cut}}
       \le C\{1+N^3(1+\log N)+|p|N^2\}\|A\|_{\mathrm{cut}}.
 \quad}
 \tag{31}
\]
The same bound holds for the inverse \(R^{-p}\). Indeed
the diagonal blocks are unitary and the off-diagonal norm
is at most \(2\|\mathscr D_N\|+|p|\|\mathscr V\|\).
This treats the exact integer power directly, rather than
multiplying a one-step bound \(|p|\) times.
In the covariant norm the sharper elementary bound is
\[
       \|R^pA\|_{\mathrm{cov}}
                    \le(1+|p|\|\mathscr V\|)\|A\|_{\mathrm{cov}}.
 \tag{32}
\]
The content of (17) is that the actual polynomial Ward
channels themselves have only polynomial loss relative
to these original physical jets.

The prescribed closing is retained, rather than selected
to match this positive norm:
\[
 \boxed{\quad
 \phi_N(A)=(Y_A^0-\mathscr D_NL_A)(c_0)
       +\mathbf1_{\mathrm{odd}}s_A
       =Y_A^0(c_0)+\mathbf1_{\mathrm{odd}}s_A.
 \quad}
 \tag{33}
\]
To see this, use the original full trace
\(\phi_N(A)=\eta\sum_{j<m}(a_jA'(c_j)-c_jA(c_j))
+\mathbf1_{\mathrm{odd}}A(-2)\), and
\(F_j(c_0)=K_N(c_j,c_0)=1\).
Moreover \(K_N(w,c_0)=1\), so \(G_j(c_0)=0\).
Full-jet equivalence in (5) and \(Q(c_0)=0\) give
\(Z_j(c_0)=0\). Thus the entire image of \(\mathscr D_N\)
vanishes at \(c_0\), proving the second equality.
The exact evaluation norm on \(\mathcal P_m\) is
\[
 \sum_{j<m}\frac{|F_j(c_0)|^2}{h_j}
       =4\sin\theta\sum_{j<m}\sin((2j+1)\theta)
       =4\sin^2(m\theta)\le4.
 \tag{34}
\]
Consequently
\[
 |\phi_N(A)|\le
 \sqrt{4\sin^2(m\theta)+\mathbf1_{\mathrm{odd}}}\,
       \min\{\|A\|_{\mathrm{cov}},\|A\|_{\mathrm{cut}}\}.
 \tag{35}
\]
The displayed constant is the exact dual norm for either
positive norm: the coordinates in (29) are arbitrary, so
the evaluation functional and the independent simple
coordinate attain their Hilbert dual norm. It equals \(2\)
at even levels and is at most \(\sqrt5\) at odd levels.
This remains an upper observation estimate, not a lower
bound on any prescribed source.

## 6. Scope and complete direct sources

The formulas apply to arbitrary actual received inputs,
including canonical products of previously received sources.
They do not bound the cost of forming those products.
Free spectator coefficients may be retained in the exact
identities; the positive norms refer to any fixed complex
specialization of them.

The crossing in (23) is multiplication by \(R^p\).
It is not the turn \(T\), nor
\(V_p=\kappa^pTR^{-p}T\). No operator estimate for either
of those maps in (27) has been proved here. In particular
the theorem does not contradict the existing obstruction
to a positive full-space norm invariant under \(V_1\).
It also does not convert the indefinite original closing
into a positive pairing, prove noncancellation, or pay a
prescribed parent action. The coherent kernel (22) and
normal commutator (23) preserve the data needed for such
an oscillatory analysis.

All three complete direct texts were read and their used
implications checked at the following pins:

* [Positive Ward measure and coherent Cauchy tail](research_positive_ward_measure_and_coherent_cauchy_tail.md),
  SHA256 18d2aa9142806d0acd744abbbb412843acd35bf18015b8c6fc73b23428a75096:
  full source representative, positive cut measure,
  orthogonality, whole-keyhole orientation and growth.
* [Physical Jacobi charge boundary](research_physical_jacobi_charge_boundary.md),
  SHA256 530425b0c4504f2512954438465deb6d9a6e322fa58c641b6c678161baae6583:
  original finite determinant, pre-fold coefficients
  and fixed-height Ward bound.
* [Confluent row closing](research_confluent_row_closing_and_positive_quotient.md),
  SHA256 daf5760f74dbd9d9c9646a1a18b95cdffc1f42ebc3cbcfc0a1b9f79b2ad77251:
  exact full Gram, physical crossing values and normals,
  original Frobenius trace and signed conventions.

Only written proof, source-text reads and metadata hashes
were used. No mathematical program, numerical experiment,
test, build or compilation was run. Frozen source notes
and public manuscripts are unchanged.
