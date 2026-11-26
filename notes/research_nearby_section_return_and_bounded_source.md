# Nearby section return and a bounded source homotopy

Private written proof, 19 November 2026.

A change of section parameter by a factor \(e^{-s/N}\) has a bounded
actual return matrix. Its effect on the bounded quotient source is
exactly one insertion of the original total \(F\)-commutator. The
corresponding source homotopy has polynomial meridian-normal cost,
without applying a right inverse of \(F_\Sigma\).

The original pointed source is retained by its explicit \(E\)- and
\(F\)-corrections. Those older corrections do not acquire polynomial
bounds from the new homotopy. The result controls transport within
the bounded source family; it does not assert that a geometric
localization has a small current.

The two complete directs are S, the full section theorem, and B,
the bounded quotient-source theorem. Their pins are below.

## 1. The actual return

Fix \(m\ge2\), \(r=m-1\), \(N\ge2\), \(d=N-1\), and
\[
 c=2\pi i,\qquad Q=e^{c/N},\qquad M=e^\mu,\qquad
 x=-M e^{-c/(2N)},\qquad f_n=(Q;Q)_n .
 \tag{1}
\]
All matrix norms use the physical occupation coefficient basis as
an orthonormal basis. On each head,
\[
 F e_a=(1-Q^{a+1})e_{a+1},\quad Fe_d=0,\qquad
 K e_a=xQ^{-a}e_a.
\]
The actual total \(F\)-arrow, which raises occupation, is
\[
 B(M)=F_\Sigma(M)=
 \sum_{j=1}^m K_1^{-1}\cdots K_{j-1}^{-1}F_j .
 \tag{2}
\]
S proves \(B^N=0\), with all caps and for every \(M\ne0\), including
even and composite levels. Define
\[
 E_N(Z)=\sum_{n=0}^{N-1}\frac{Z^n}{f_n},\qquad
 b=a e^{-s/N},\qquad
 T_N(a,s,M)=E_N(bB)E_N(aB)^{-1}.
 \tag{3}
\]
Every Euler matrix here is invertible because it is the identity
plus a nilpotent polynomial. The inverse is an actual finite matrix.

The original quotient map and section in S and B satisfy
\[
 q_F B=0,\qquad q_F i_0=I,\qquad
 i_a=E_N(aB)i_0 .
 \tag{4}
\]
Consequently
\[
 T_N i_a=i_b,\qquad q_FT_N=q_F,\qquad
 T_{\gamma b}T_{ba}=T_{\gamma a},
 \tag{5}
\]
where \(\gamma\) is another section parameter and the notation means
the literal ratios
\(T_{ba}=E_N(bB)E_N(aB)^{-1}\). These exact identities do not
identify \(i_0\) with a vector annihilated by \(B\).

There is a fixed small meridian disk on which every fixed derivative
of \(B\) has norm bounded independently of \(N\). Indeed
\[
 B(M)=\sum_{j=1}^m M^{-(j-1)} B_j(1),\qquad
                         \|B_j(1)\|\le2 .
 \tag{6}
\]
Thus we may choose an activity disk so that
\[
                  \|aB(M)\|\le\rho<1
 \tag{7}
\]
on a larger parameter buffer. All estimates below hold for bounded
complex \(s\). The activity restriction is a restriction on actual
matrix norm, not on an unproved coherent symbol.

## 2. Holomorphic return functions and actual commutators

S's finite logarithm gives a scalar representative for (3):
\[
 f_N(z;s)=\exp\left(
   \sum_{k=1}^{N-1}
       \frac{e^{-sk/N}-1}{k(1-Q^k)}z^k\right),\qquad
                         T_N=f_N(aB;s).
 \tag{8}
\]
The scalar function is entire; the evaluation in a nilpotent matrix
depends only on its first \(N\) coefficients. Set
\[
 f_\infty(z;s)=(1-z)^{-s/c},\qquad
 T_\infty=f_\infty(aB;s),\qquad
 g_N(z;s)=\frac{f_N(z;s)-1}{z},\qquad
 g_\infty(z;s)=\frac{f_\infty(z;s)-1}{z}.
 \tag{9}
\]
Both divided functions extend at \(z=0\). The logarithm defining
\(f_\infty\) is its convergent series in \(|z|<1\). The model
\(T_\infty\) still uses the actual \(N\)-dependent matrix \(B(M)\).

For any fixed disk \(|z|\le R<1\) and bounded \(s\),
\[
 \begin{split}
 |f_N-1|+|g_N|+|g_\infty|&\le C_R|s|,\\
 |f_N-f_\infty|+|g_N-g_\infty|&\le C_R|s|/N .
 \end{split}
 \tag{10}
\]
Here and below constants may depend on the fixed \(s\)-buffer.
To see the uniform factor \(|s|\), write the logarithm in (8)
and its difference from
\(-\frac{s}{c}\log(1-z)\). For \(k\le N/2\),
\[
 \left|
 \frac{e^{-sk/N}-1}{k(1-Q^k)}-\frac{s}{ck}
 \right|\le C|s|/N.
 \tag{11}
\]
This follows by removing the singularity at zero of
\((e^{-st}-1)/(1-e^{ct})\). For \(k>N/2\) the first coefficient
is at most \(C|s|/(N-k)\). Multiplication by \(R^k\) pays that
whole upper half and the missing infinite logarithmic tail.
Exponentiating the bounded logarithms proves the estimates for
\(f\); their vanishing difference at zero and a slightly larger
disk prove the estimates for \(g\). No cyclic alias is removed.

Choose \(\rho<R<1\) inside this buffer and put
\(\mathcal R(z)=(zI-aB)^{-1}\). Its norm on \(|z|=R\) is at most
\((R-\rho)^{-1}\). For any matrix \(C\), holomorphic functional
calculus gives the exact identity
\[
 [C,f(aB)]=\frac{a}{2\pi i}
     \int_{|z|=R} f(z)\mathcal R(z)[C,B]\mathcal R(z)\,dz .
 \tag{12}
\]
It follows by commuting \(C\) with the resolvent; the integral of
the constant function contributes zero to this commutator.
The ideal inequality
\(\|AXB\|_\nu\le\|A\|\,\|X\|_\nu\,\|B\|\), for
\(\nu=\mathrm{op}\) or trace norm \(1\), proves
\[
 \boxed{\begin{split}
 \|[C,T_N]\|_\nu
       &\le C|as|\,\|[C,B]\|_\nu,\\
 \|[C,T_N-T_\infty]\|_\nu
       &\le C|as|N^{-1}\,\|[C,B]\|_\nu .
 \end{split}}
 \tag{13}
\]
In addition, if \(G_N=g_N(aB;s)\) and
\(G_\infty=g_\infty(aB;s)\), then
\[
 \|G_N\|+\|G_\infty\|\le C|s|,\qquad
 \|G_N-G_\infty\|\le C|s|/N .
 \tag{14}
\]
These bounds use the same actual resolvents and are independent of
the matrix dimension. The return and its inverse are uniformly
bounded, as is their comparison with the corresponding model,
by (8)--(11).

Equations (6),(12) also pay the true meridian derivatives without
a loss of \(N\) from the return itself. For fixed \(k\), differentiating
the resolvents gives
\[
 \begin{split}
 \|\partial_\mu^kG_N\|&\le C_k|s|,\\
 \|\partial_\mu^k(G_N-G_\infty)\|&\le C_k|s|/N,\\
 \|\partial_\mu^k[C,T_N]\|_\nu
  &\le C_k|as|\sum_{j=0}^k\|\partial_\mu^j[C,B]\|_\nu .
 \end{split}
 \tag{15}
\]
The last row has the additional factor \(N^{-1}\) for
\(T_N-T_\infty\). All derivatives hold \(Q,a,s\) fixed.
Derivatives of an \(M\)-dependent mark \(C\) remain in the
displayed actual current; they have not been bounded implicitly.

## 3. A bounded homotopy of the original quotient source

We recall only B's actual matrices needed here. Let
\(V=(\mathbb C^N)^{\otimes m}\), \(U=(\mathbb C^N)^{\otimes r}\).
B constructs a holomorphic bounded section \(j:U\to V\) with
\[
 q_Fj=I,\quad P=jq_F,\quad \ker P=\operatorname{im}B .
 \tag{16}
\]
Here \(J_ie_a=ae_a\), \(K_{\rm r}=K_2\cdots K_m\) is the tail
Cartan, \(K_\Sigma=K_1\cdots K_m\), and
\(\Phi(C)=\operatorname{Tr}((P_0\otimes g)C)\) is the original
pointed source, with \(P_0=|0\rangle\langle0|\) and
\(g=K_{\rm r}^{-d}\). Put
\[
 D_N(z)=\frac{z^N-z^{-N}}{z-z^{-1}},\qquad
 H=D_N(MK_{\rm r}),\qquad H_{\rm tot}=D_N(-e^{c/(2N)}K_\Sigma).
\]
The meromorphic quotient coupon is
\[
 Q_{\rm b}=D_N(M)jH^{-1}q_F .
 \tag{17}
\]
Apparent singularities are interpreted by the same meromorphic
continuation as the original source. In particular
\[
 Q_{\rm b}B=0,\qquad
 \sup_{|N\mu|\le\eta}\|\mu Q_{\rm b}\|\le C_{m,\eta},
 \quad
 \sup_{|N\mu|\le\eta}\|\mu Q_{\rm b}\|_1\le C_{m,\eta}N^r
 \tag{18}
\]
for \(\eta<\pi/m\). On a smaller buffered collar its \(k\)-th
regularized true derivative costs at most \(C_kN^k\).

Define the nearby section and coupon by
\[
 j_s=T_Nj,\qquad P_s=T_NP,\qquad
 Q_s=T_NQ_{\rm b}=D_N(M)j_sH^{-1}q_F .
 \tag{19}
\]
Since \(q_FT_N=q_F\), these satisfy
\[
 q_Fj_s=I,\qquad P_s^2=P_s,\qquad
 \ker P_s=\operatorname{im}B,\qquad Q_sB=0 .
 \tag{20}
\]
For example \(PT_N=P\), proving the projector identity.
Both \(j_s\) and \(\mu Q_s\) are bounded on the specified buffers.
The new section generally changes total integer occupation.
Thus (19) does not assert
\(Q_s=D_N(M)H_{\rm tot}^{-1}P_s\); the order in (19) is essential.

There is an explicit homotopy with no division by \(B\):
\[
 \boxed{\quad
 \mathcal V_s=-aG_NQ_{\rm b},\qquad
 [\mathcal V_s,B]=Q_s-Q_{\rm b}.
 \quad}
 \tag{21}
\]
Indeed \(T_N-I=aBG_N\), \(G_NB=BG_N\), and \(Q_{\rm b}B=0\).
Hence \(\mathcal V_sB=0\) and
\(B\mathcal V_s=-(T_N-I)Q_{\rm b}\).
In particular
\[
 \|\mu\mathcal V_s\|\le C|as|,\qquad
 \|\mu\mathcal V_s\|_1\le CN^r|as|,\qquad
 \|\partial_\mu^k(\mu\mathcal V_s)\|
                         \le C_kN^k|as| .
 \tag{22}
\]
These are polynomial source costs for this actual change of section.
They contain no norm of \(q_F\) or of a right inverse of \(B\).
Replacing \(G_N,T_N\) by \(G_\infty,T_\infty\) gives the same exact
homotopy identities for the model coupon. Its regularized difference
from (21) is \(O(|as|/N)\) in operator norm.

The change also has a uniformly bounded square-zero realization.
For a fixed reference section \(P\), put
\[
 \mathscr N_s=(T_N(a,s)-I)P,\qquad
 \mathscr U_s=I+\mathscr N_s .
 \tag{22a}
\]
Since \(P(T_N-I)=0\), for every two parameters in the stated buffer,
\[
 \mathscr N_s\mathscr N_t=0,\qquad
 \mathscr U_s^{-1}=I-\mathscr N_s,\qquad
 \|\mathscr N_s\|\le C|as|,
\]
\[
 \mathscr U_sj=j_s,\qquad
 \mathscr U_sQ_{\rm b}\mathscr U_s^{-1}=Q_s .
 \tag{22b}
\]
For the last identity use \(PQ_{\rm b}=Q_{\rm b}P=Q_{\rm b}\)
and \(Q_{\rm b}(T_N-I)=0\). All fixed true meridian jets of
\(\mathscr N_s\) have polynomial cost on the collar. This upgrades
the algebraic section change in B with a bound for the actual
completed Euler family.

For every actual total intertwiner \(W\), (17) and the original
quotient identity give
\[
 \operatorname{Tr}(Q_sW)=\operatorname{Tr}(Q_{\rm b}W)=\Phi(W).
 \tag{23}
\]
Here \(W\) commutes with \(B\), hence with \(T_N\), and
\(Q_{\rm b}T_N=Q_{\rm b}\). This is an equality of the original
source and all its true meridian derivatives, with external lines
retained.

## 4. A single current and all root normals

For an arbitrary analytic mark \(C(M)\), put \(J=[C,B]\).
The stronger, matrix-valued identity is
\[
 \boxed{\quad
 Q_{\rm b}C(T_N-I)=Q_{\rm b}[C,T_N]
                         =aQ_{\rm b}J G_N .
 \quad}
 \tag{24}
\]
For the second equality expand
\([C,BG_N]=[C,B]G_N+B[C,G_N]\) and use \(Q_{\rm b}B=0\).
Thus the quotient-source change is exactly
\[
 \Delta_N(C):=\operatorname{Tr}((Q_s-Q_{\rm b})C)
      =\operatorname{Tr}(Q_{\rm b}C(T_N-I))
      =a\operatorname{Tr}(Q_{\rm b}J G_N).
 \tag{25}
\]
This is a literal insertion of the original \(F_\Sigma\)-current.
For a mark followed by a total intertwiner, \(C=C_0W\), one has
\(J=[C_0,B]W\), with its order unchanged.

There is an exact grading simplification for closed marks.
Let \(\mathsf J=\sum_iJ_i\) denote total integer occupation.
Both \(Q_{\rm b}\) and \(P_0\otimes g\) preserve it, whereas
\(T_N-I\) is a sum of strictly positive powers of the degree-one
operator \(B\). Consequently, if \([\mathsf J,C]=0\), then
\[
       \Delta_N(C)=0,\qquad \Phi(C(T_N-I))=0 .
 \tag{25a}
\]
The trace of each positive-degree term is zero. The quantitative
return estimate is relevant to marks or windows that mix these
degrees. Neither (25a) nor that estimate makes the unclosed
commutator \([C,B]\) zero.

Pointwise on the punctured meridian collar, (14),(18) imply
\[
 |\mu\Delta_N(C)|
 \le C|as|\min\{\|J\|_1,\ N^r\|J\|\}.
 \tag{26}
\]
The regularized function is holomorphic across \(\mu=0\).
For a uniform jet statement choose
\(\eta<\eta'<\pi/m\), and let
\[
 \mathcal M_N=
 \min\left\{\sup_{|N\mu|\le\eta'}\|J\|_1,\quad
               N^r\sup_{|N\mu|\le\eta'}\|J\|\right\}.
 \]
Buffered Cauchy estimates give
\[
 \sup_{|N\mu|\le\eta}
 |\partial_\mu^k(\mu\Delta_N(C))|
                      \le C_kN^k|as|\mathcal M_N .
 \tag{27}
\]
Writing \(\Delta_\infty(C)=a\operatorname{Tr}
(Q_{\rm b}JG_\infty)\), the corresponding comparison is
\[
 \sup_{|N\mu|\le\eta}
 |\partial_\mu^k[\mu(\Delta_N-\Delta_\infty)]|
                      \le C_kN^{k-1}|as|\mathcal M_N .
 \tag{28}
\]
In particular the \(O(N^{-1})\) comparison is a statement about
the regularized family. A finite-part comparison has only an
\(O(1)\) bound from (28); it is not automatically \(O(N^{-1})\).

The exact root row keeps the current normal and the moving return.
Write the actual Taylor expansions:
\[
 Q_{\rm b}=\mu^{-1}R_{\rm b}+C_{\rm b}+O(\mu),\quad
 J=J_0+\mu J_1+O(\mu^2),\quad
 G_N=G_0+\mu G_1+O(\mu^2).
 \]
Then
\[
 \boxed{\begin{split}
 \operatorname{Res}_{\mu=0}\Delta_N
    &=a\operatorname{Tr}(R_{\rm b}J_0G_0),\\
 \operatorname{FP}_{\mu=0}\Delta_N
    &=a\operatorname{Tr}
      (C_{\rm b}J_0G_0+R_{\rm b}J_1G_0+R_{\rm b}J_0G_1).
 \end{split}}
 \tag{29}
\]
Here \(C=C_0+\mu C_1+\cdots\), and
\(J_1=[C_1,B_0]+[C_0,B_1]\). For example the exact derivative
of the return factor is
\[
 G_1=\frac{a}{2\pi i}\int_{|z|=R}
       g_N(z;s)(zI-aB_0)^{-1}B_1(zI-aB_0)^{-1}\,dz .
 \tag{30}
\]
No commutativity of \(B_0\) and \(B_1\) is assumed.
Higher source coefficients are the corresponding finite convolutions.
Their bound from (27) is \(C_jN^{j+1}|as|\mathcal M_N\) for the
coefficient of \(\mu^j\), \(j\ge-1\); (28) saves one power of \(N\).
Separate residues in (29) need not vanish for a marked window.

The transported source and its new homotopy have equally explicit
root data. If \(T_N=T_0+\mu T_1+\cdots\), then
\[
 \begin{split}
 \operatorname{Res}Q_s&=T_0R_{\rm b},&
 \operatorname{FP}Q_s&=T_0C_{\rm b}+T_1R_{\rm b},\\
 \operatorname{Res}\mathcal V_s&=-aG_0R_{\rm b},&
 \operatorname{FP}\mathcal V_s
       &=-a(G_0C_{\rm b}+G_1R_{\rm b}).
 \end{split}
 \tag{30a}
\]
Thus the bounded section change retains the true first normal of
both the source and its return, even when the leading residue
contribution vanishes only after a complete pairing.

## 5. The original pointed functional remains explicit

B supplies the actual total arrow \(E=E_\Sigma\), the specified
meromorphic homotopies \(\mathcal W_E,\mathcal V_F\), and the matrix row
\[
 P_0\otimes g-Q_{\rm b}
       =[\mathcal W_E,E]+[\mathcal V_F,B],
 \qquad g=K_{\rm r}^{-d}.
 \tag{31}
\]
Combining it with (21) gives, for every analytic mark,
\[
 \boxed{\begin{split}
 \Phi(C)&=\operatorname{Tr}((P_0\otimes g)C)\\
 &=\operatorname{Tr}(Q_sC)
   +\operatorname{Tr}(\mathcal W_E[E,C])
   +\operatorname{Tr}((\mathcal V_F-\mathcal V_s)[B,C]).
 \end{split}}
 \tag{32}
\]
This is an exact meromorphic identity whose full right side has
the same analytic continuation as the original left side.
It pays the source change rather than replacing the source by
an arbitrary trace. Equation (22) bounds only the added homotopy
\(\mathcal V_s\); the existing \(\mathcal W_E,\mathcal V_F\)
still have B's proved exponential costs.

For completeness, the original error of a transported marked window
is also exact:
\[
 \begin{split}
 \Phi(C(T_N-I))={}&\Delta_N(C)\\
 &+\operatorname{Tr}\mathcal W_E
       \bigl([E,C](T_N-I)+C[E,T_N]\bigr)\\
 &+\operatorname{Tr}\mathcal V_F[B,C](T_N-I).
 \end{split}
 \tag{33}
\]
The \(B\)-row uses \([B,T_N]=0\); the \(E\)-row has both terms.
Although (13) applies to \([E,T_N]\) as well, its right side
contains the actual \([E,B]\), not a zero current.
Thus (26) alone is not a bound for the complete expression (33).

Every equality (21)--(33) holds throughout the actual whole-meridian
family at the fixed quantum root. Taking all Laurent coefficients
retains the moving arrows, return, pivot and source coupons.
A prescribed analytic outside scalar can be absorbed into \(C\);
its derivatives then appear in \(J\) and (29). For a meromorphic
outside line its complete Laurent multiplication must instead be
retained. No separate residue is silently discarded.

The parameter change \(b-a=O(N^{-1})\) does not make \(T_N-I\)
of that size: its model is \((I-aB)^{-s/c}-I\). The controlled
quantity is its actual Ward insertion. Nor do the bounded estimates
for a fixed \(s\)-buffer justify an uncosted composition of \(O(N)\)
steps to a finite classical displacement. In particular the fixed
reference transformations in (22) compose additively:
\(\mathscr U_s\mathscr U_tj=(T_s+T_t-I)j\), which is not in general
\(T_sT_tj\). A step relative to a new section instead carries that
section's norm. Small current data,
geometric chart matching and the original closing-cycle estimate
are not supplied by this theorem.

## Complete proof-source pins

* S: notes/research_full_section_coalescent_kernel.md,
  576 lines, SHA256
  c26240d060f4474d3d59baae0c44c58dff60dcd550cf184defaadec5760509c7.
* B: notes/research_bounded_quotient_source_and_ward_homotopy.md,
  456 lines, SHA256
  a105d3b6aa2848ba14f978566d8f7bfeff3741910eef3ffe056fb02e972a5da7.

Both complete directs were freshly whole-read nontruncated in this
author sequence. The entire matching final was read back, every used
implication checked, and all three hashes renewed before freezing.
Only written mathematics and text/hash operations were used; frozen
and public files were not edited.
