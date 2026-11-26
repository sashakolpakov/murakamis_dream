# Forced source transport to the opposite-polarization kernel

Private written proof, 18 November 2026.

An arbitrary finite marked word has an exact reduction to the actual
opposite-polarization kernels, with two explicit Ward currents. The
original highest cut and all tail pivots remain in the formula. No
intertwining condition is imposed on a vacuum coupon or on a restricted
coherent resolution.
An explicit Jordan solver bounds the grouped marked source currents
by a simple meridian pole, so their finite parts use at most first
meridian jets. No corresponding uniform norm bound is assumed.

Equivalently, the original source coupon and the opposite-quotient
source differ by an explicitly constructed sum of total \(E\)- and
\(F\)-commutators. This is a co-source homotopy before scalar closure.
It transports the literal beta vacuum forcing through a specified
finite Cauchy network, but does not identify that forcing with the
polar residue of the opposite kernel or prove its cancellation.

The complete directs C, H, J, B, and K are pinned at the end. C and H
supply the actual prefix matrices and scalar adjoint kernel; J supplies
the opposite-polarization operators. The forced first-column
reconstruction, its combined co-source, and the marked incidence
formulas below are proved here.

## 1. The original source and a forced first-column recursion

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and \(m\ge2\)
actual heads at their common meridian \(M\) near one. The quantum
parameter is fixed throughout. Write
\[
 x=-M/q,\qquad f_n=\prod_{j=1}^n(1-Q^j),\qquad f_0=1,
 \qquad g=K_{\rm r}^{\,1-N}.
 \tag{1}
\]
Here the subscript \({\rm r}\) denotes the ordered remaining \(m-1\)
heads. All \(f_n\), \(n<N\), are nonzero. Let \(i_n:U\to V\) and
\(p_n:V\to U\) insert and extract first occupation \(n\), respectively.
The prescribed source for an arbitrary analytic matrix \(A(M)\) is
\[
\Phi(A)=\operatorname{Tr}_V((P_0\otimes g)A),\qquad
P_0=|0\rangle\langle0|,\quad i_0p_0=P_0\otimes I.
 \tag{2}
\]
Any external scalar framing, dimension, or peripheral line stays
attached to both sides of every identity.

C gives the literal triangular matrix
\[
 S=\sum_{n=0}^d\frac{(x^{-1}L_1F_{\rm r})^n}{f_n},
 \qquad S^{-1}F_\Sigma S=F_1,
 \qquad E':=S^{-1}E_\Sigma S=E_{\rm r}+L_1b_A,
 \tag{3}
\]
\[
 b_n=MK_{\rm r}Q^{-n}-M^{-1}K_{\rm r}^{-1}.
 \tag{4}
\]
The first-head lowering shift is \(L_1w_a=w_{a-1}\), with its missing
bottom arrow zero. The \(b_A\) in (3) is evaluated at the input
occupation. In particular \(E'i_0=i_0E_{\rm r}\).

Put
\[
 A'=S^{-1}AS,\qquad C_n=f_n^{-1}p_nA'i_0,\qquad
 Y_j=f_j^{-1}p_jS^{-1}[E_\Sigma,A]Si_0.
 \tag{5}
\]
These are analytic matrices on \(U\); no commutation of \(A\) with
\(F_\Sigma,K_\Sigma\), or \(E_\Sigma\) has been used. Since
\(S^{-1}i_0=i_0\), the original source sees exactly this first column:
\[
 \boxed{\quad
 \Phi(A)=\sum_{n=0}^d
       \operatorname{Tr}_U(x^{-n}gF_{\rm r}^{\,n}C_n).
 \quad}
 \tag{6}
\]
Indeed only the \(n\)-th lowering term of \(p_0S\) returns
\(f_n i_nC_n\) to first occupation zero. Its coefficient
\(x^{-n}F_{\rm r}^n/f_n\) cancels \(f_n\).

For \(1\le n\le d\), the first-column coefficient of
\([E',A']\), divided by \(f_{n-1}\), is
\[
 Y_{n-1}=[E_{\rm r},C_{n-1}]
                  +(1-Q^n)b_nC_n.
 \tag{7}
\]
The top coefficient is \(Y_d=[E_{\rm r},C_d]\). It is retained as
an identity, although it is not needed to reconstruct the first
column upward.

Choose a punctured meridian disk where every \(b_n\) is invertible.
Such a disk exists: each diagonal entry is a difference of two
nonzero monomials \(cM^m-c'M^{-m}\), and every zero at one is simple.
Define the ordered maps
\[
 a_n=(1-Q^n)b_n,\qquad
 \mathscr D_n(X)=-a_n^{-1}[E_{\rm r},X],\qquad
 \mathscr D_n^*(Z)=[E_{\rm r},Za_n^{-1}].
 \tag{8}
\]
Cyclicity of the ordinary matrix trace proves that the displayed
\(\mathscr D_n^*\) is the adjoint of \(\mathscr D_n\). Equation (7)
becomes the exact forced recursion
\[
 C_n=\mathscr D_n(C_{n-1})+a_n^{-1}Y_{n-1}.
 \tag{9}
\]
Thus the homogeneous commutant calculation extends to every
marked matrix by retaining the first-column Ward forcing.

## 2. The explicit current kernels

For \(1\le j\le d\), define a matrix on the remaining heads by
\[
 \boxed{\quad
 \mathcal K_j=
 \sum_{n=j}^d
 \left(\mathscr D_{j+1}^*\circ\cdots\circ\mathscr D_n^*\right)
                (x^{-n}gF_{\rm r}^{\,n})\,a_j^{-1}.
 \quad}
 \tag{10}
\]
An empty composition is the identity. Composition has its usual
right-to-left meaning; the final \(a_j^{-1}\) is on the right.
Iteration of (9), followed by the trace adjoints in (8), gives
\[
 \Phi(A)=\operatorname{Tr}_U(\mathcal H C_0)
                 +\sum_{j=1}^d\operatorname{Tr}_U(\mathcal K_jY_{j-1}),
 \tag{11}
\]
\[
 \mathcal H=\sum_{n=0}^d
   (\mathscr D_1^*\circ\cdots\circ\mathscr D_n^*)
                   (x^{-n}gF_{\rm r}^{\,n}).
 \tag{12}
\]
For example a forcing at level \(j\) first enters as
\(a_j^{-1}Y_{j-1}\), then passes through
\(\mathscr D_{j+1},\ldots,\mathscr D_n\); this verifies every order
in (10).

H proves a universal rational identity for the matrix (12),
not merely its value on admissible constant terms:
\[
 \mathcal H=D_N(M)H^{-1},\qquad
 H=D_N(MK_{\rm r}),\qquad
 D_N(z)=\frac{z^N-z^{-N}}{z-z^{-1}}.
 \tag{13}
\]
The Laurent-polynomial continuation defines \(D_N\) at \(\pm1\).
H's identity retains the full remaining Casimir, including its
Jordan blocks, before its Casimir dependence cancels. Consequently
it applies to the arbitrary \(C_0\) in (5). We obtain
\[
 \boxed{\quad
 \Phi(A)=D_N(M)\operatorname{Tr}_U(H^{-1}C_0)
                 +\sum_{j=1}^d\operatorname{Tr}_U(\mathcal K_jY_{j-1}).
 \quad}
 \tag{14}
\]
There is no reset of a marked word to a homogeneous intertwiner.

All matrices in (10) are explicitly meromorphic. Since every
\(b_n^{-1}\) has pole order at most one, \(\mathcal K_j\) has pole
order at most \(d-j+1\). The complete right side of (14) has the
removable continuation of (2). Individual summands need not be
removable. These potentially deep poles can be avoided for the
grouped current by the following explicit construction.

### A simple-pole primitive for the full marked current

Define the homogeneous first-column source coupon
\[
 Q_{\rm h}=D_N(M)i_FH^{-1}q_F,\qquad
 i_F=i_0,\quad q_F=p_0S^{-1},\qquad
 Q_E=P_0\otimes g-Q_{\rm h}.
 \tag{14a}
\]
Equation (14) shows that
\(\operatorname{Tr}(Q_EA)=0\) for every matrix commuting with
\(E_\Sigma\). This uses no \(F_\Sigma\)- or Cartan-commutation:
then all \(Y_j\) in (5) vanish, which is sufficient.

Let \(\mathscr C(M)\) be J's full balanced turnover. It obeys
\(E_\Sigma(M)\mathscr C(M)
=\mathscr C(M)F_\Sigma(M^{-1})\) and is holomorphic invertible
near one. On the first head let \(D_fw_a=f_aw_a\), and put
\[
 \mathcal U_E=\mathscr C(M)S(M^{-1})(D_f\otimes I).
 \tag{14b}
\]
The root prefix identity and
\(D_f^{-1}F_1D_f=\mathsf U\), where
\(\mathsf Uw_a=w_{a+1}\) for \(a<d\) and \(\mathsf Uw_d=0\),
give
\[
 E_\Sigma\mathcal U_E=\mathcal U_E(\mathsf U\otimes I).
 \tag{14c}
\]
All these changes of basis are holomorphic invertible at \(M=1\);
their conditioning as \(N\) varies is not estimated here.

Write \(\widehat Q_E=\mathcal U_E^{-1}Q_E\mathcal U_E\) in \(N\)-by-\(N\)
blocks on \(U\). Test its trace against
\(\mathsf U^k\otimes B\), for arbitrary \(B\in\operatorname{End}(U)\).
The corresponding conjugated matrix commutes with \(E_\Sigma\).
Nondegeneracy of the ordinary trace on \(U\) therefore gives
\[
       \sum_{i=0}^{d-k}(\widehat Q_E)_{i,i+k}=0,\qquad 0\le k\le d.
 \tag{14d}
\]
Define a linear, parameter-independent solver by
\[
 (\mathcal X_E)_{i0}=0,\qquad
 (\mathcal X_E)_{i,j+1}=(\widehat Q_E)_{ij}+(\mathcal X_E)_{i-1,j}
       \quad(0\le j<d),\qquad (\mathcal X_E)_{-1,j}=0.
 \tag{14e}
\]
For \(j<d\), this says
\([\mathcal X_E,\mathsf U\otimes I]_{ij}=(\widehat Q_E)_{ij}\).
For \(j=d\), the missing equation is
\[
 (\widehat Q_E)_{i,d}+(\mathcal X_E)_{i-1,d}
   =\sum_{s=0}^i(\widehat Q_E)_{s,d-i+s}=0,
 \]
which is exactly (14d) for \(k=d-i\).
Thus the full last column, including both corners, is retained.
Set
\[
 \boxed{\qquad
 \mathcal W_E=\mathcal U_E\mathcal X_E\mathcal U_E^{-1},\qquad
 Q_E=[\mathcal W_E,E_\Sigma].
 \qquad}\tag{14f}
\]

Both \(Q_{\rm h}\) and \(\mathcal W_E\) have at most a simple
meridian pole. Indeed on a physical \(K_0\)-weight \(\chi\),
\[
 H^{-1}=
 \frac{M^m\chi-M^{-m}\chi^{-1}}
 {\varepsilon(M^{mN}-M^{-mN})},\qquad
 \varepsilon=(-1)^{(N+1)(m-1)}.
 \]
The denominator has a simple zero, and (14b),(14e) add no
meridian poles. Consequently the forced source also has the
bounded-depth form
\[
 \boxed{\quad
 \Phi(A)=D_N(M)\operatorname{Tr}_U(H^{-1}C_0)
           +\operatorname{Tr}_V(\mathcal W_E[E_\Sigma,A]).
 \quad}\tag{14g}
\]
The finite parts of these two grouped terms require only the
value and first meridian derivative of the analytic marked
family, with all derivatives of its actual changes of basis
included. Their residues need not vanish separately. This is
an exact improvement of the initial recursion; it is not a
uniform norm bound on \(\mathcal W_E\).

## 3. The actual opposite-polarization defect

Retain J's balanced turnover \(\mathscr C(M):V(M^{-1})\to V(M)\),
including tensor reversal, its original diagonal factors, and all
their meridian derivatives. Use the short notation
\[
 q_+=p_0S(M)^{-1},\quad i_+=i_0,\qquad
 q_-=p_0S(M^{-1})^{-1},\quad i_-=i_0.
 \tag{15}
\]
In particular \(\ker q_\pm=F_\Sigma(M^{\pm1})V\).
On one head put
\[
 \lambda_Fw_a=
 \begin{cases}
 (1-Q^a)^{-1}w_{a-1},&a>0,\\
 0,&a=0,
 \end{cases}
 \qquad
 \Lambda_F=S(\lambda_F\otimes I)S^{-1}.
 \tag{16}
\]
The direct identities \(F_1\lambda_F=I-P_0\) and (3) give
\[
               F_\Sigma\Lambda_F=I-i_+q_+.
 \tag{17}
\]
This is the actual finite partial inverse; it does not invert
the nilpotent \(F_\Sigma\).

For the given marked matrix \(A\), set
\[
 A^\vee=\mathscr C(M)^{-1}A(M)\mathscr C(M),\quad
 B_+=q_+Ai_+=C_0,\quad B_-=q_-A^\vee i_-.
 \tag{18}
\]
\(A^\vee\) acts on the reflected space. Thus every mark, and not
only the braid word, is transported. J's actual operators are
\[
 T=q_+E_\Sigma^d\mathscr C i_-,\qquad J=H^{-1}T,\qquad
 J_{\rm ref}=J(M^{-1}),
 \tag{19}
\]
\[
 \gamma_N=(-1)^dD_N(M)/N,\qquad
 a_N=(-1)^dN\gamma_N^m,\qquad
 JJ_{\rm ref}=a_NH^{-1},\qquad TJ_{\rm ref}=a_NI.
 \tag{20}
\]
In the last equality use \(HT=TH(M^{-1})\) and
\(TT(M^{-1})=a_NH\), as proved in J.

The reduced marked defect has the following full-head expression:
\[
 \boxed{\begin{split}
 \Delta_A&:=B_+T-TB_-\\
 &=q_+\left([A,E_\Sigma^d]
       -[A,F_\Sigma]\Lambda_FE_\Sigma^d\right)\mathscr C i_-.
 \end{split}}\tag{21}
\]
To prove it, insert \(i_+q_+=I-F_\Sigma\Lambda_F\) in \(B_+T\).
In \(TB_-\), replace \(i_-q_-\) by \(I\): its difference has
image in the reflected \(F_\Sigma V\), which
\(E_\Sigma^d\mathscr C\) kills because
\(\mathscr C F_\Sigma(M^{-1})=E_\Sigma(M)\mathscr C\) and
\(E_\Sigma^N=0\). The remaining terms use
\(A\mathscr C=\mathscr C A^\vee\) and
\(q_+AF_\Sigma=q_+[A,F_\Sigma]\). This proves the sign and order
in (21). Also
\[
 [A,E_\Sigma^d]=
       \sum_{k=0}^{d-1}E_\Sigma^k[A,E_\Sigma]E_\Sigma^{d-1-k}.
 \tag{22}
\]

J's matrix sewing identity, or direct use of (19)--(21), gives
\[
 J B_-J_{\rm ref}=a_NH^{-1}B_+
                                  -H^{-1}\Delta_AJ_{\rm ref}.
 \tag{23}
\]
Combining this with (14) proves the full marked source formula
\[
 \boxed{\begin{split}
 \Phi(A)=\frac{D_N(M)}{a_N}\operatorname{Tr}_U
       \left(JB_-J_{\rm ref}+H^{-1}\Delta_AJ_{\rm ref}\right)
       +\sum_{j=1}^d\operatorname{Tr}_U(\mathcal K_jY_{j-1}).
 \end{split}}\tag{24}
\]
The two corrections in (24) are different: the last sum repairs
the pointed source reduction, while \(\Delta_A\) repairs opposite
polarization. Neither is suppressed for arbitrary marks.

## 4. An explicit co-source homotopy and its sewing law

The corrections in (24) factor through the original total
commutators. Put
\[
 c_N=\frac{D_N(M)}{a_N},\qquad
 Z=\mathscr C i_-J_{\rm ref}H^{-1}q_+,
 \tag{25}
\]
\[
\mathcal V_E=
 \mathcal W_E-c_N\sum_{k=0}^{d-1}E_\Sigma^{d-1-k}ZE_\Sigma^k,
 \qquad
 \mathcal V_F=c_N\Lambda_FE_\Sigma^dZ.
 \tag{26}
\]
These are fixed meromorphic matrices on \(V\), independent of \(A\).
The rectangular trace identity and cyclicity, applied to (14g),
(21), and (22), prove
\[
 \boxed{\quad
 \Phi(A)-c_N\operatorname{Tr}_U(JB_-J_{\rm ref})
  =\operatorname{Tr}_V\!
       \left(\mathcal V_E[E_\Sigma,A]
                         +\mathcal V_F[F_\Sigma,A]\right).
 \quad}
 \tag{27}
\]
For the sign, (21) contains
\(-\sum E_\Sigma^k[E_\Sigma,A]E_\Sigma^{d-1-k}
 +[F_\Sigma,A]\Lambda_FE_\Sigma^d\).
Moving its outside factors through the trace gives precisely
the second term of \(\mathcal V_E\) and \(\mathcal V_F\).

There is an equivalent matrix identity between source coupons:
\[
 \boxed{\quad
 P_0\otimes g-P_{\rm opp}
       =[\mathcal V_E,E_\Sigma]+[\mathcal V_F,F_\Sigma],
 \quad}
 \tag{28}
\]
\[
 P_{\rm opp}
   =c_N\mathscr C i_-J_{\rm ref}Jq_-\mathscr C^{-1}.
 \tag{29}
\]
Indeed \(\operatorname{Tr}(P_{\rm opp}A)\) is the paired term
in (27), by (18), and the ordinary trace pairing on all matrices
is nondegenerate. This proves (28) without an abstract identification
of two unipotent monodromies.
In fact
\[
 P_{\rm opp}=D_N(M)\mathscr C i_-H(M^{-1})^{-1}q_-\mathscr C^{-1},
 \tag{29a}
\]
so it too has at most a simple meridian pole. The grouped paired
functional and its complete correction in (27) therefore use at
most first meridian jets. The displayed primitives (26), or
separate unresolved products of two \(J\)'s, can have higher
poles; their cancellations must be carried out before asserting
that bound. Relative windows do not inherit it automatically.

For a literal sewn word \(A=A_L\cdots A_1\), the currents propagate by
\[
 [G,A]=\sum_{\ell=1}^L
       A_L\cdots A_{\ell+1}[G,A_\ell]A_{\ell-1}\cdots A_1,
 \qquad G=E_\Sigma,F_\Sigma.
 \tag{30}
\]
With different ordered stage spaces, replace the local bracket by
\(G_{\ell}A_\ell-A_\ell G_{\ell-1}\); the same telescoping proves
the formula. Actual crossings cancel these rows by their coproduct
intertwining. A marked coupon retains its own row. If the crossing
is further expanded into nonintertwining Euler or factorial atoms,
all their rows remain until that complete crossing is recombined.
Thus (27)--(30) are compatible with the original incidence
contraction, including intermediate basis changes.

The finite Cauchy kernel
\(K_A(z,w)=\sum_{\alpha,\beta}A_{\alpha\beta}z^\alpha w^{-\beta}\)
has exact composition by constant term in every paired head.
This follows just by matching the exponents. The source kernel on
the opened head is \(1\), representing \(P_0\); every other closing
head retains \(\sum_{a=0}^d g_a(z_{\rm in}/z_{\rm out})^a\).
In particular an averaged or all-ones cut from another presentation
is not substituted in a marked identity.
The same matrix rows may instead be resolved by J's compact
coherent identity. Every finite projector and every complementary
chain is then retained. These are exact realizations of (27),
not an assertion that a geometric window has zero defect.

## 5. The literal beta vacuum and its retained norm period

B supplies the actual reflected trivalent coefficient with
\[
 p_a=\frac{(-1)^aQ^{a(a-1)/2}}{f_a},\qquad m_a=\frac{Q^a}{f_a}.
 \tag{31}
\]
Writing its radial variable as \(r\), its coefficient equation is
\[
 [r^0]\,r^d\Psi_-(\log U-\log r)
                 \Psi_+(\log V-\log r)\Psi_+(-\log r)
  =\frac{Q^{-d}}N B_N(Q^2U,QV),
 \tag{32}
\]
\[
 B_N(u,v)=\sum_{a=0}^d\prod_{j=0}^{a-1}(u-Q^jv),\qquad
 B_N(u,v)-(u-v)B_N(u,Qv)=1-u^N+v^N.
 \tag{33}
\]
The coefficient array on the left of (32) is
\(m_a p_b p_cU^aV^b\), with \(a+b+c=d\).
Its constant term in \(U,V\) is exactly the atomic state
\((a,b,c)=(0,0,d)\), with coefficient
\[
                     p_d=Q/N=Q^{-d}/N.
 \tag{34}
\]
Here \(f_d=N\) and
\((-1)^dQ^{d(d-1)/2}=Q\). Thus the unit in (33), before its
displayed normalization is removed, is an explicit atomic
vacuum coupon, with this scalar.
K's original factorial reflection replaces the third atomic
order \(c\) by physical order \(d-c\); the distinguished order
is therefore zero on that head. This statement identifies the
indices and normalization; it does not replace the surrounding
three-port contraction by an identity on the physical heads.

More precisely, keep the entire prescribed exterior and its
finite Cauchy contractions. Replacing the three-port coefficient
array by the single state (34) defines a specific marked matrix
\(A_{\rm vac}\) at the original open cut, or a scalar if that
cut is already closed. The analogous replacements by \(u^N\)
and \(v^N\) in (33) define the two shifted rows in the same
ambient coefficient space. All affine indices and zero
extensions are retained. Linearity sends (33) to the exact
corresponding identity of these sewn matrices.
It is not permissible to drop the shifted rows before checking
their actual exterior support or their continued contour.

Apply (24) or (27) separately to each such finite marked matrix.
This gives its original source as a paired \(J\)-kernel term
and the explicit currents (5),(10),(21), or equivalently (26).
There is no claim that \(A_{\rm vac}\) is an intertwiner.
Already on a single head,
\[
 [E,P_0]=-(MQ^{-1}-M^{-1})|0\rangle\langle1|,\qquad
 [F,P_0]=(1-Q)|1\rangle\langle0|.
 \tag{35}
\]
The original fusion in K is \(C_{\rm fus}=S_2F_1^{\rm diag}\),
where \(F_1^{\rm diag}\) has entries \(f_a\).
For example the transported vacuum has the explicit row
\[
 P_0S^{-1}
 =P_0+\sum_{k=1}^d
    \frac{(-1)^kQ^{k(k-1)/2}x^{-k}}{f_k}
                  |0\rangle\langle k|\otimes F_{\rm r}^k,
 \qquad S(P_0\otimes I)=P_0\otimes I.
 \tag{36}
\]
The \(P_0\) on the left of (36) is also tensored with \(I\).
This follows from the finite inverse of (3); it displays the
extra coproduct coupons rather than resetting that row to \(P_0\).

The balanced norm-pole contribution is also retained. If
\(\mathfrak d=1-u^N+v^N\), the Newton products satisfy
\(p_{a+N}^{\rm Newt}=(u^N-v^N)p_a^{\rm Newt}\).
Where the block geometric series converges, and then by its
rational continuation, their untruncated sum is
\[
 \mathcal F_N=\frac{B_N}{\mathfrak d}
       =\frac{\mathcal S_N}{\mathfrak d}+\mathcal I_N,
 \qquad
 \mathcal F_N(u,v)-(u-v)\mathcal F_N(u,Qv)=1.
 \tag{37}
\]
The second equality uses B's exact Barnes decomposition on
\(\Im u<0,\ \Im(v/u)>0\), with its specified continuation.
Its balanced block \(\mathcal S_N\) is nonzero there, while
\(\mathcal I_N\) is the retained Barnes normalization term.
Equivalently, the affine
one-step transport of \((\mathcal F_N,1)^t\) has full-orbit matrix
\[
 \prod_{j=0}^{N-1}
 \begin{pmatrix}u-Q^jv&1\\0&1\end{pmatrix}
 =\begin{pmatrix}u^N-v^N&B_N(u,v)\\0&1\end{pmatrix}.
 \tag{38}
\]
The product is in the order obtained by successive substitution
in (37). On a balanced point \(\mathfrak d=0,\ uv\ne0\),
\(B_N\ne0\), so this is a nontrivial unipotent extension.
The rational splitting \(B_N/\mathfrak d\) has its compulsory
norm pole.

Equations (37)--(38) concern that local scalar source and its
specified continuation. They do not assert that the global
Verma closing determinant is a product of local \(\mathfrak d\)'s.
Nor does (27) identify \(\mathfrak d=0\) with \(M=1\), identify
the beta vacuum with the residue of \(J\), or discard
\(\mathcal I_N\). Such statements would require further actual
incidence and relative-cycle identities.

## 6. Continuation and scope

All reductions were proved on a punctured fixed-root meridian disk.
For analytic finite \(A\), their complete right sides have the
analytic continuation of (2). At \(M=1\) take the finite part of
the entire equality, in one fixed coordinate such as \(\log M\).
For a separate summand with nonzero residue, finite parts in
\(M-1\) and \(\log M\) need not agree; no coordinate change is
made term by term without its correction.
No residue or higher-jet term of a separate unresolved correction
is deleted. Equations (14f)--(14g) and (29a) prove a first-jet
bound for the grouped marked co-sources themselves; they do not
impose the homogeneous first-jet cancellations of H and J on
individual current terms or relative kernel windows.

The result is an explicit source homotopy with the original
pivots and actual opposite-polarization operators. It applies
to any fixed actual word and finite insertions, including a word
obtained after a prescribed short partial filling. It estimates
neither its current matrices nor their periods. Quantum-parameter
normals require the additional off-root prefix wall and the
unchanged whole pivot/framing adapters; they are not covered by
these fixed-\(q_N\) formulas. No positive geometric contour,
vanishing complementary chain, or nonzero geometric coefficient
is inferred.

## Complete proof directs

* C: notes/research_prefix_commutant_and_pointed_normal_functional.md,
  SHA256 b4fb801a1482316aebb4799f1d0b80d5b43ced39138d903c04cfde811ca166b0.
* H: notes/research_scalar_prefix_kernel_and_first_meridian_jet.md,
  SHA256 d7d82848a1b3f50709352905bafcc7ddfee36f41e434bf5de4663b4b6181dc9e.
* J: notes/research_opposite_polarization_source_kernel.md,
  SHA256 d52c6dd8e62f575a262fc7af460e258f7cb0e40b5a9c037ac46dd8d151002d44.
* B: notes/actual_trivalent_quantum_beta_source.md,
  SHA256 b290a73a123cc5f76fad12c087c11a61ba9c6fd77130ead3637b852a84ca996b.
* K: notes/actual_euler_gaussian_cauchy_network.md,
  SHA256 8ed7102043d69b442400748447dd91d1093ca1b678b6ae6acbdefaec1904317f.

All five complete directs were freshly read nontruncated in this
active author sequence. Every used implication and source order
was checked. Only written mathematics and text/hash operations
were used; frozen and public files were not changed.
