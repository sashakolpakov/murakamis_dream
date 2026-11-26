# The opposite source's two-step normal lattice

Private written proof, 18 November 2026.

On every regular total-Cartan block, the actual opposite kernel is a
matrix factorization of the meridian parameter. Its holomorphic
unnormalized map has only unit and simple-zero factors. The residue
of the normalized map identifies one graded piece; its finite part,
taken modulo that residue image, identifies the other. Together these
are invertible, with explicit inverses furnished by the actual
reflected kernel. A moving input retains its first-normal correction.

This is a finite-level statement about the original source maps,
at every fixed width and level. It is not uniform ellipticity in
the level, a coherent-kernel lower bound, or transport of a selected
relative cycle. The complete directs J and L are pinned below.

## 1. The two actual degree blocks and their common scalar

Use J's conventions
\[
 N\ge2,\quad d=N-1,\quad r=m-1,\quad m\ge2,\quad
 q=e^{\pi i/N},\quad Q=q^2,\quad M=e^\mu.
 \tag{1}
\]
The quantum root is fixed. Write \(D=rd\), and let \(U_k\) be the
remaining-head space of total integer occupation \(k\). Its root
Cartan weight is
\[
 \chi_k=(-q^{-1})^rQ^{-k},\qquad
 \chi_{D-k}=\chi_k^{-1},\qquad
 \chi_k^N=\varepsilon:=(-1)^{(N+1)r}.
 \tag{2}
\]
Fix \(k\) with \(\chi_k^2\ne1\), and put \(k^*=D-k\).
The spaces \(V=U_{k^*}\) and \(W=U_k\) have the same dimension,
by complementing every occupation. No noninteger degree is used.

J defines the analytic map and its original normalization
\[
 T(M)=q_F(M)E_\Sigma(M)^d\mathscr C_m(M)i_F(M^{-1}),
 \qquad J_{\rm op}(M)=H(M)^{-1}T(M),
 \quad H(M)=D_N(MK_{\rm r}(M)),
 \tag{3}
\]
where \(D_N(z)=(z^N-z^{-N})/(z-z^{-1})\).
The degree rule is \(T(M)U_j\subset U_{D-j}\).
On the two fixed spaces define the analytic blocks
\[
 T_k(\mu):V\longrightarrow W,\qquad
 S_k(\mu):W\longrightarrow V,\qquad
 S_k(\mu)=T_{k^*}(-\mu).
 \tag{4}
\]
Thus a prime on \(S_k\) includes the minus sign from the reflected
meridian. All blocks retain the original ordered physical bases.

The scalar appearing in both compositions is the same:
\[
 \begin{split}
 H_k(\mu)&=D_N(e^{m\mu}\chi_k)=\mu h_k(\mu),\\
 a(\mu)&=(-1)^dN
       \left((-1)^dD_N(e^\mu)/N\right)^m,\\
 T_kS_k&=aH_kI_W,\qquad S_kT_k=aH_kI_V.
 \end{split}\tag{5}
\]
Indeed J proves the first composition. For the second, its reflected
formula has \(a(-\mu)\) and \(H_{k^*}(-\mu)\). The first is \(a(\mu)\);
the second is \(D_N((e^{m\mu}\chi_k)^{-1})=H_k(\mu)\).
This checks the scalar on the correct domain, rather than identifying
the two degree blocks without reflection.

Both \(a\) and \(h_k\) are holomorphic units. Their root values are
\[
 a_0=(-1)^{d(m+1)}N,\qquad
 h_0=\frac{2\varepsilon mN}{\chi_k-\chi_k^{-1}}\ne0.
 \tag{6}
\]
For example, expand
\[
 H_k(\mu)=
 \frac{\varepsilon(e^{mN\mu}-e^{-mN\mu})}
 {e^{m\mu}\chi_k-e^{-m\mu}\chi_k^{-1}}.
 \tag{7}
\]
This is the reason for restricting to \(\chi_k^2\ne1\).
Self-reciprocal Cartan blocks do not have this simple-zero scalar.

Let \(\mathcal O\) be the ring of holomorphic germs at \(\mu=0\),
and use the same letters \(V_{\mathcal O},W_{\mathcal O}\) for the
free modules of analytic vector germs. Set
\[
 b(\mu)=a(\mu)h_k(\mu),\qquad F(\mu)=b(\mu)^{-1}S_k(\mu).
 \]
Then the exact source equations become
\[
             T_kF=\mu I_W,\qquad FT_k=\mu I_V.
 \tag{8}
\]
These are equations of analytic matrices, not just of leading symbols.

## 2. A direct lattice proof, without a normal-form theorem

We prove the needed linear algebra from (8). Write
\[
 T_k=T_0+\mu T_1+O(\mu^2),\qquad
 F=F_0+\mu F_1+O(\mu^2),
 \]
and define the intrinsic root subspaces
\[
               K=\ker T_0\subset V,\qquad I=\operatorname{im}T_0
                    \subset W.
 \tag{9}
\]
At orders zero and one, (8) gives
\[
 T_0F_0=F_0T_0=0,\quad
 T_1F_0+T_0F_1=I_W,\quad
 F_1T_0+F_0T_1=I_V.
 \tag{10}
\]
If \(v\in K\), the last identity says \(v=F_0T_1v\).
If \(F_0w=0\), the preceding identity says \(w=T_0F_1w\).
Consequently
\[
                K=\operatorname{im}F_0,\qquad I=\ker F_0.
 \tag{11}
\]
In particular the root two-periodic complex is exact.

There are two canonical isomorphisms:
\[
 \begin{split}
 \alpha &:V/K\longrightarrow I,\qquad [v]\longmapsto T_0v,\\
 \beta &:K\longrightarrow W/I,\qquad v\longmapsto[T_1v].
 \end{split}\tag{12}
\]
The first is immediate. The inverse of the second is the map
\([w]\mapsto F_0w\): (10) proves both inverse identities.
Equivalently, for any analytic lift \(v(\mu)\) of \(v\in K\),
\[
             \beta(v)=[\,(\mu^{-1}T_kv(\mu))|_{\mu=0}\,].
 \tag{13}
\]
Replacing that lift by another adds \(T_0v_1\), which lies in \(I\).
This proves independence of the lift. The parameter \(\mu=\Log M\)
has been fixed; no unrecorded choice of a normal coordinate is made.

The entire image lattice also has a canonical description:
\[
 \boxed{\quad
 \Lambda_k:=T_kV_{\mathcal O}
       =\{w(\mu)\in W_{\mathcal O}:w(0)\in I\},
 \qquad \mu W_{\mathcal O}\subset\Lambda_k\subset W_{\mathcal O}.
 \quad}\tag{14}
\]
The inclusion from left to right is immediate. Conversely choose a
constant vector \(v_0\) with \(T_0v_0=w(0)\). Then
\(w-T_kv_0=\mu w_1\), and (8) gives
\(w=T_k(v_0+Fw_1)\). This proves equality, including every
higher Taylor coefficient.

Choose a constant basis \(w_1,\ldots,w_p\) for \(I\), and complete it
to a basis of \(W\). Equation (14) shows that
\[
             w_1,\ldots,w_p,\ \mu w_{p+1},\ldots,\mu w_n
 \tag{15}
\]
is an \(\mathcal O\)-basis of \(\Lambda_k\).
The map \(T_k:V_{\mathcal O}\to\Lambda_k\) is bijective:
surjectivity is its definition, and injectivity follows from
\(FT_k=\mu I\), since analytic vector germs have no \(\mu\)-torsion.
Take the preimages of (15) as the analytic basis of \(V_{\mathcal O}\).
In these two bases, the exact matrices are
\[
                    T_k=\operatorname{diag}(I_p,\mu I_{n-p}),
       \qquad F=\operatorname{diag}(\mu I_p,I_{n-p}).
 \tag{16}
\]
Thus only unit and simple-zero factors occur. This construction
proves that statement directly; it does not invoke a Smith-form
theorem. In particular
\[
 \operatorname{ord}_{\mu=0}\det T_k=\dim K,\qquad
 W_{\mathcal O}/\Lambda_k\simeq W/I
 \tag{17}
\]
as modules killed by \(\mu\). The bases in (16) are not canonical;
the lattice (14) and maps (12) are canonical.

## 3. The original normalized residue and finite part

Now retain the original \(J_{\rm op}\), rather than normalizing
\(T_k\) by a freely chosen scalar. On these spaces write
\[
 J_k(\mu)=\frac{T_k(\mu)}{\mu h_k(\mu)}
              =\frac{\mathcal R_k}{\mu}+\mathcal J_k+O(\mu).
 \tag{18}
\]
If \(h_k=h_0+\mu h_1+\cdots\), then exactly
\[
 \mathcal R_k=h_0^{-1}T_0,\qquad
 \mathcal J_k=h_0^{-1}T_1-h_1h_0^{-2}T_0.
 \tag{19}
\]
The normalized image is the enlarged lattice
\[
             J_kV_{\mathcal O}=\mu^{-1}\Lambda_k,\qquad
 W_{\mathcal O}\subset J_kV_{\mathcal O}\subset\mu^{-1}W_{\mathcal O}.
 \tag{20}
\]
Multiplication of \(\Lambda_k\) by the scalar unit \(h_k^{-1}\)
does not change it, which proves (20).

The canonical associated-graded map of this normalized source is
\[
 \boxed{\quad
 \begin{split}
 \mathfrak j_{-1}&:V/K\longrightarrow I,
                 & [v]&\longmapsto\mathcal R_kv,\\
 \mathfrak j_0&:K\longrightarrow W/I,
                 & v&\longmapsto[\mathcal J_kv].
 \end{split}
 \quad}\tag{21}
\]
It is an isomorphism on each graded piece, and hence jointly on
\((V/K)\oplus K\) and \(I\oplus(W/I)\). This is not a canonical
splitting of the original vector spaces.

The reflected operator provides explicit inverses using at most
its first derivative. Put \(S_0=S_k(0)\), \(S_1=S_k'(0)\).
Then
\[
 \boxed{\quad
 \mathfrak j_{-1}^{-1}(w)=[a_0^{-1}S_1w]\quad(w\in I),
 \qquad
 \mathfrak j_0^{-1}([w])=a_0^{-1}S_0w.
 \quad}\tag{22}
\]
Indeed differentiate \(T_kS_k=S_kT_k=\mu bI\).
For \(w\in I=\ker S_0\), \(T_0S_1w=b_0w\).
For \(v\in K\), \(S_0T_1v=b_0v\); and
\(T_1S_0w=b_0w\) modulo \(I\). Since \(b_0=a_0h_0\),
(19) gives (22). These arguments also prove that both inverse
formulas are independent of their representatives.

For an actual moving input \(v(\mu)=v_0+\mu v_1+\cdots\),
\[
 \operatorname{Res}_{\mu=0}(J_kv)=\mathcal R_kv_0,\qquad
 \operatorname{FP}_{\mu=0}(J_kv)
                  =\mathcal J_kv_0+\mathcal R_kv_1.
 \tag{23}
\]
If \(v_0\in K\), the second expression is the actual regular value.
Its class modulo \(I\) is (21), but its representative generally
depends on \(v_1\). Removing that correction would change the
physical finite part.

An analytic output frame has its corresponding correction as well.
For \(\widehat J=L(\mu)^{-1}J_kR(\mu)\), with invertible analytic
frames, write \(L=L_0+\mu L_1+\cdots\), \(R=R_0+\mu R_1+\cdots\).
Then its residue is \(L_0^{-1}\mathcal R_kR_0\), and its finite part is
\[
 L_0^{-1}\mathcal J_kR_0+
 L_0^{-1}\mathcal R_kR_1-
 L_0^{-1}L_1L_0^{-1}\mathcal R_kR_0.
 \tag{24}
\]
Thus (16) is a legitimate analytic frame description, not permission
to discard its derivatives in the original source.
If instead the finite part uses \(t=M-1\), then
\(1/\mu=1/t+1/2+O(t)\), so its constant matrix is
\(\mathcal J_k+\mathcal R_k/2\). The quotient map on \(K\)
is unchanged; unrestricted finite parts are not identical.

## 4. Matching the marked primary orders at every width

L's whole-meridian factorization of the actual Gauss operator is
\[
 A_N=\mathfrak G_N\bigl[(I-P_{\rm up})+\delta_m P_{\rm up}\bigr],
 \qquad \delta_m=1-e^{-2mN\mu}.
 \tag{25}
\]
Here \(P_{\rm up}(\mu)\) is the sum of the actual marked primary
clusters with physical labels \(l_1+l_2\ge N\), including their Jordan
parts. It is analytic at fixed \(N\); \(\mathfrak G_N\) is an
analytic invertible matrix. L proves (25) before taking any normal.
No scalar eigenvalue substitution replaces its matrix calculus.

On the present degree block, retain L's entire routing as
\[
 T_k=X_k A_N Y_k,\qquad
 X_k=\mathcal B_m(W_\tau^{-1})|_{U_k},\qquad
 Y_k=(D_{\rm top}\mathscr C_r)|_{U_{k^*}}.
 \tag{26}
\]
Both factors are analytic isomorphisms near the root:
the braid and its reduced inverse are actual inverses, \(D_{\rm top}\)
is an invertible degree scalar, and turnover has the unit square
recorded in J. They map the indicated degree spaces in the displayed
order. Put \(Z_k=X_k\mathfrak G_N\), and abbreviate \(P=P_{\rm up}|_{U_k}\).
Equations (25),(26) identify the intrinsic spaces (9) explicitly:
\[
              K=Y_k(0)^{-1}\operatorname{ran}P(0),\qquad
              I=Z_k(0)\operatorname{ran}(I-P(0)).
 \tag{27}
\]
This includes every primary present at that width, not merely a
chosen simple spectral channel.

There is an exact moving-upper realization of the second map in (21).
Take \(p_0\in\operatorname{ran}P(0)\), set \(p(\mu)=P(\mu)p_0\),
and use the actual input \(v(\mu)=Y_k(\mu)^{-1}p(\mu)\). Then
\[
 J_k(\mu)v(\mu)=
       \frac{\delta_m(\mu)}{H_k(\mu)}Z_k(\mu)p(\mu),
 \qquad
 \frac{\delta_m}{H_k}
 =\frac{e^{m\mu}\chi_k-e^{-m\mu}\chi_k^{-1}}
             {\varepsilon e^{mN\mu}}.
 \tag{28}
\]
Thus the product is holomorphic and
\[
 (J_kv)(0)=
       \frac{\chi_k-\chi_k^{-1}}{\varepsilon}Z_k(0)p_0\ne0
                \quad\hbox{if }p_0\ne0.
 \tag{29}
\]
Its class modulo \(I\) is precisely \(\mathfrak j_0(v_0)\).
The equality of its representative with (23) retains both the
projector derivative and the \(Y_k^{-1}\) derivative.

For the lower primaries the corresponding moving input has residue
\(h_0^{-1}Z_k(0)(I-P(0))p_0\).
Consequently the lattice's two orders are exactly L's lower
unit and upper first-normal orders after the literal routing.
In particular
\[
                   \dim K=\operatorname{rank}P_{\rm up}(0).
 \tag{30}
\]
No primary space has disappeared when its unnormalized root value
vanishes. Its first normal supplies the other invertible graded map.

## 5. Intertwiners, the closing functional, and the quantitative limit

For an actual unmarked braid, J proves
\[
 B_+(\mu)T_k(\mu)=T_k(\mu)B_-( -\mu).
 \tag{31}
\]
It follows at the root that the input word preserves \(K\), the output
word preserves \(I\), and \(\alpha\) intertwines their induced maps.
Differentiate (31) on \(v\in K\), then reduce modulo \(I\).
The term with the derivative of \(B_-\) is in \(I\), and the term
with \(B_+'T_0v\) is zero. Hence \(\beta\), and therefore both
normalized graded maps (21), intertwine the root actions as well.
Their chosen finite-part representatives still contain the first
normal terms; this quotient statement does not remove them.
For arbitrary marks or windows, the exact defect
\(B_+T_k-T_kB_-\) remains and need not preserve these subspaces.

The original paired source is still J's expression
\[
 \Phi_0(W)=\frac{D_N(M)}{a_N(M)}
   \operatorname{Tr}\!\left(
     J_{\rm op}(M)B_-(M^{-1})J_{\rm op}(M^{-1})\right).
 \tag{32}
\]
All Cartan weights, degree blocks, moving coupons, exterior factors,
and the original analytic continuation are retained. The first-normal
depth established here concerns the lattice of a single opposite map.
An arbitrary windowed product of two meromorphic kernels can still
have a double pole; its finite part can involve higher derivatives.
J's assembled first-jet trace cancellation is a separate exact
identity, not a consequence of replacing (32) by the two graded maps.

At a fixed level the admissible analytic bases of each lattice are
related by invertible matrices over \(\mathcal O\). This is the
ordinary freedom of frames of the specified source lattice.
The physical section (3) and scalar (5) remain fixed. Equations
(23),(24),(28) say how a change of frame acts on its normal data.
There is no new choice of the normalization of a period.

No estimate here bounds the norm of such frames, their inverses,
the primary projectors, or their derivatives as \(N\) grows.
Even \(h_0^{-1}=(\chi_k-\chi_k^{-1})/(2\varepsilon mN)\)
does not control the remaining matrix factors. The lattice theorem
therefore proves neither uniform microlocal ellipticity nor
nonvanishing of a closed trace or a geometric relative-cycle
coefficient. It supplies a concrete finite-level object to which
such a comparison would have to be compatible.

## Complete directs and coverage

* J: notes/research_opposite_polarization_source_kernel.md,
  639 lines, SHA256
  d52c6dd8e62f575a262fc7af460e258f7cb0e40b5a9c037ac46dd8d151002d44.
* L: notes/research_marked_gauss_functional_calculus.md,
  487 lines, SHA256
  7f8c7c0be05331e7c0679c5a26374bbcb4b38b817c36a1f4ac4e16d4c1739095.

J already proves the source composition, square-zero residue,
contracting homotopy, degree reflection and first-jet closing row.
L already proves the marked primary factorization (25).
The degree-scalar frame and finite dualizing-residue notes were
coverage reads, not additional proof inputs. The addition here is
the canonical image lattice, its direct two-factor normal form,
the two normalized graded isomorphisms with reflected inverses,
and their explicit identification with the moving original source.
No general novelty is claimed for matrix-factorization linear algebra.

Only written mathematics and text operations are used. The entire
matching final and both complete directs were read nontruncated in this
active author sequence; an initially truncated combined J output was
recovered through its entire ending. Every used implication was checked
and all three pins renewed. Independent matching review and parent
adoption remain separate. Frozen and public files are unchanged.
