# The actual braid-axis trace, its filling, and its integer-degree twist action

Private written proof, 19 November 2026.

There is one finite polynomial whose prescribed two evaluations recover
the original pointed source, including its first meridian normal. Its
degree variable records the exact highest degree after the actual
prefix reduction. This gives a signed full-twist action by an explicit
Gaussian operator on that polynomial. The corresponding rational
twisted fixed scheme is the marked braid-axis scheme with closure
multiplier equal to the polynomial variable.

The two-Cartan source formula by itself is already available, for
example in research_reduced_common_spin_first_jet_dual.md. That is
background coverage, not an additional proof input here. The finite
polynomial, its uncollapsed twist action, and the variable-meridian
scheme comparison are assembled below from the six complete directs
R, W, G, M, B and A pinned at the end. No asymptotic coefficient or
noncancellation follows merely from this assembly.

## 1. The finite polynomial and its original marking

Fix an integer \(N\ge2\), and put
\[
 d=N-1,\qquad q=e^{\pi i/N},\quad Q=q^2,\quad
 M=e^\mu,\quad x=-M/q.
 \tag{1}
\]
The quantum parameter stays fixed while the actual meridian varies.
Let \(m\ge2\), \(r=m-1\), and let \(W_\beta(M)\) be the original
finite braid operator on \(V_N(M)^{\otimes m}\), including every
crossing scalar \(\kappa(M)\). The remaining space is
\(U=V_N(M)^{\otimes r}\). In its original occupation basis define
\[
 Jw_{a_1}\otimes\cdots\otimes w_{a_r}
       =(a_1+\cdots+a_r)w_{a_1}\otimes\cdots\otimes w_{a_r},
 \qquad 0\le a_i\le d.
 \tag{2}
\]
Thus \(J\) has integer values from \(0\) to \(rd\), not values
modulo \(N\). Write \(U_j=\ker(J-j)\).

R supplies the actual prefix and quotient
\[
 S_m=\sum_{n=0}^d\frac{(x^{-1}L_1F_{\rm r})^n}{f_n},\quad
 f_n=(Q;Q)_n,\quad
 \mathcal B_m(X)=p_0S_m^{-1}Xi_0,
 \tag{3}
\]
where \(i_0v=w_0\otimes v\), \(p_0\) extracts that row, and
\(L_1w_a=w_{a-1}\), with its zero endpoint. On actual whole-meridian
total intertwiners, \(\mathcal B_m\) is an algebra map. The prefix
preserves the full integer occupation sum. Consequently an
integer-degree-preserving intertwiner has image commuting with \(J\).

We allow a marked operator \(O(M)\) which is an analytic actual
total intertwiner and preserves that same integer degree. B's fixed
loop-observable words are examples. Set
\[
 B_{O,\beta}(M)=\mathcal B_m(O(M)W_\beta(M)),\qquad
 T_{O,\beta,N}(s,M)=\operatorname{Tr}_U(s^JB_{O,\beta}(M))
                  =\sum_{j=0}^{rd}t_j(M)s^j,
 \quad t_j=\operatorname{Tr}_{U_j}B_{O,\beta}.
 \tag{4}
\]
Every term is finite. The coefficients are holomorphic on the chosen
meridian domain of the actual word and mark. For \(O=I\), abbreviate
this to \(T_\beta\). Integer-degree-preserving braid conjugation,
with the mark conjugated along with the word, leaves (4) unchanged:
use the algebra map in (3), commutation with \(s^J\), and ordinary
trace cyclicity.

For arbitrary \(s\), (4) is a defined ordinary trace family. We do
not assert that \(s^J\) has a holomorphic lift to a total intertwiner
at completeness. The original pointed evaluation is the specific
functional on this polynomial proved next.

## 2. Exact filling and its true meridian jet

Put
\[
 a=Mx^r,\qquad c=(-q^{-1})^r,\qquad
 \varepsilon=c^N=(-1)^{(N+1)r},\qquad a=ce^{m\mu},
 \quad D_N(z)=\frac{z^N-z^{-N}}{z-z^{-1}}.
 \tag{5}
\]
The actual remaining Cartan is \(K_{\rm r}=x^rQ^{-J}\).
R's source identity therefore gives, with \(T=T_{O,\beta,N}\),
\[
 \boxed{\quad
 \Phi_{O,\beta}(M)
 :=\operatorname{Tr}_{\rm full}
   ((P_0\otimes K_{\rm r}^{1-N})O W_\beta)
 =\frac{D_N(M)}{a^N-a^{-N}}
        \bigl[aT(Q^{-1},M)-a^{-1}T(Q,M)\bigr].
 \quad}\tag{6}
\]
Indeed \((MK_{\rm r})^N=a^NI\), while
\(MK_{\rm r}=aQ^{-J}\). Substituting these into
\(D_N(M)/D_N(MK_{\rm r})\) proves (6) term by term in the
original tail basis. This uses the original pivot, not an
ordinary trace substituted for that pivot. All self-Cartan
sectors are included.

Define
\[
 T_-(\mu)=T(Q^{-1},e^\mu),\quad T_+(\mu)=T(Q,e^\mu),\qquad
 \Lambda(\mu)=ce^{m\mu}T_-(\mu)-c^{-1}e^{-m\mu}T_+(\mu).
 \tag{7}
\]
Then (6) is exactly
\[
 \Phi_{O,\beta}(e^\mu)
  =\frac{\sinh(N\mu)}{2\varepsilon\sinh\mu\sinh(mN\mu)}
                                                    \Lambda(\mu).
 \tag{8}
\]
The original finite expression in (6) is analytic. Its removable
root pole imposes the specified residue identity
\[
                       cT_-(0)=c^{-1}T_+(0).
 \tag{9}
\]
Its finite part is
\[
 \boxed{\quad
 \Phi_{O,\beta}(1)
 =\frac{cT_-(0)+c^{-1}T_+(0)}{2\varepsilon}
  +\frac{cT_-'(0)-c^{-1}T_+'(0)}{2\varepsilon m}.
 \quad}\tag{10}
\]
Here the prime is the true derivative in \(\mu\) at fixed \(q\).
Both sample points remain fixed. It differentiates the actual
prefix, word, mark and crossing scalars. In particular (10) is
not determined by the root polynomial alone.

All higher true jets are retained by the same identity. On
\(|\mu|<b/N\), \(0<b<\pi/m\), inside the chosen word domain, set
\[
 h_N(\mu)=\frac{\mu\sinh(N\mu)}
                  {2\varepsilon\sinh\mu\sinh(mN\mu)}.
 \tag{11}
\]
This is holomorphic and even, with \(h_N(0)=1/(2\varepsilon m)\).
Equations (8)--(9) give the holomorphic expression
\(\Phi=h_N\Lambda/\mu\). Thus a source jet of order \(k\)
uses the polynomial family through meridian order \(k+1\), with
ordinary finite Taylor multiplication. Other zeros of
\(\sinh(mN\mu)\) are not discarded by a fixed-size collar claim.

There is an important limit to (9). If both sample points are
multiplied by an arbitrary \(s\), the corresponding meromorphic
row has residue
\[
 \frac{cT(Q^{-1}s,1)-c^{-1}T(Qs,1)}{2\varepsilon m}.
 \tag{12}
\]
It need not vanish. The actual cancellation in (9) is at the
prescribed filling \(s=1\); (4) remains holomorphic independently.
We do not manufacture a holomorphic two-variable pointed source
by subtracting (12) without retaining that current.

If the source convention has an outside line \(\Xi_N(M)\), including
a marked peripheral or modified-dimension factor, it multiplies
every term of (6)--(10). For zero framing also retain
\[
       \alpha(M)^{-w},\qquad \alpha=\kappa x^{-d},
                    w=\operatorname{wr}(\beta).
 \tag{13}
\]
Such a line may be absorbed into \(T\) when analytic, or left
explicit; its whole germ is multiplied before taking derivatives
or removable limits. In particular
\(\partial_\mu\log\alpha=\partial_\mu\log\kappa-d\).

## 3. Highest degrees give the exact signed full-twist action

Let \(\Gamma=\Delta_m^2\), \(L=m(m-1)\), and remove exactly its
\(L\) positive crossing scalars:
\[
                         Z_m=\kappa^{-L}W_\Gamma.
 \tag{14}
\]
The following identifies the degree label without using a root
Casimir projector. R proves \(S_m^{-1}F_\Sigma S_m=F_1\).
Therefore
\[
 V_N(M)^{\otimes m}/F_\Sigma V_N(M)^{\otimes m}
                   \ \xrightarrow{\ p_0S_m^{-1}\ }\ U
 \tag{15}
\]
is an isomorphism preserving exact degree. It is defined throughout
the actual meridian family; the quotient is free because \(S_m\)
conjugates its image to the constant-rank image of \(F_1\).
The action induced by any total intertwiner is precisely (3).

For generic \(M\), W proves a decomposition into length-\(N\)
highest strings with highest-degree multiplicities
\((1+z+\cdots+z^d)^r\). In each string, quotienting by \(F_\Sigma\)
leaves its highest vector and kills its positive descendants.
If that vector has integer degree \(j\), (15) puts it in \(U_j\).
W's scalar on every multiplicity copy is
\(x^{-2mj}Q^{j(j-1)}\). Consequently
\[
 \boxed{\qquad \mathcal B_m(Z_m)
                    =x^{-2mJ}Q^{J(J-1)}.\qquad}\tag{16}
\]
Both sides are actual analytic finite matrices. Generic equality
extends through every meridian collision, including all true jets.
The generic strings and their projectors are not separately
specialized at a collision.

On polynomials of degree at most \(rd\), let \(D=s\partial_s\) and
define the finite Gaussian operator by its monomial action
\[
             \mathcal H_n=Q^{nD(D-1)},\qquad
             \mathcal H_n(s^j)=Q^{nj(j-1)}s^j,
                            \quad n\in\mathbb Z.
 \tag{17}
\]
This definition needs no infinite heat series or convergence limit.
For a fixed mark \(O\) as in Section 1, (16) commutes with its
reduced matrix. The algebra map gives the exact action
\[
 \boxed{\quad
 T_{O,\Gamma^n\beta,N}(s,M)
       =\kappa(M)^{nL}\,
          \mathcal H_n T_{O,\beta,N}(x(M)^{-2mn}s,M).
 \quad}\tag{18}
\]
Negative \(n\) uses the literal inverse; every diagonal scalar
in (16) is a unit. Equation (18) is valid for all finite caps,
even and composite levels, and every allowed meridian jet.

Although the phase in (17) is periodic in \(j\) modulo \(N\),
the whole multiplier is not: at \(j+N\) versus \(j\) its ratio
is \(M^{-2mnN}\). The root values coincide, but their logarithmic
meridian slopes differ by \(-2mnN\). The polynomial and the
dilation in (18) therefore retain the full integer degree.
No residue-class sum replaces its coefficients.

For example differentiation of (18) gives the operator
\[
  \partial_\mu+nL\,\partial_\mu\log\kappa-2mnD
 \tag{19}
\]
on the original family before applying its displayed Gaussian
and dilation. For the zero-framed polynomial
\(\overline T_\beta=\alpha^{-w}T_\beta\), the corresponding row is
\[
 \overline T_{\Gamma^n\beta}(s,M)
       =x^{dnL}\mathcal H_n
                    \overline T_\beta(x^{-2mn}s,M),
 \tag{20}
\]
whose first derivative retains \(n(dL-2mD)\). The same prescribed
outside line is retained on both sides when it is part of the
normalization. Equations (6) and (18) give the actual filled
source of every signed full twist, without replacing its source
normal by a root semisimple substitution.

## 4. Two exact endpoint coefficients

For an unmarked braid word, (4) is nonzero and has degree exactly
\(rd\). In fact
\[
                 [s^0]T_\beta=\kappa^w,\qquad
                 [s^{rd}]T_\beta=\kappa^wM^{-2dw}.
 \tag{21}
\]
Both degree spaces have dimension one. For an internal positive
generator the all-vacuum coefficient is \(\kappa\). At the all-top
input its recipient cannot be raised, so only zero Euler transfer
survives, with coefficient
\(\kappa x^{-2d}Q^{d^2}=\kappa M^{-2d}\), since \(d(d+1)=dN\).
For the boundary generator R gives
\(\mathcal B_m(R_1)=\kappa S_rD_{\rm red}\), where
\(D_{\rm red}w_a=(-1)^aQ^{a(a-1)/2}x^{-2a}w_a\).
The Euler prefix is the identity on both extreme degree spaces;
its top diagonal is \(M^{-2d}\) by the same identity.
Inverses invert these two scalars. Multiplication proves (21).

This is nontriviality of the finite family, not of its geometric
part. The linear filling in Section 2 may cancel. No nonzero
endpoint statement is asserted for an arbitrary inserted mark.

There is also an exact root exchange relation. It records a cyclic
shadow without replacing the integer-degree polynomial. The actual
total Casimir from W is
\(\Omega_\Sigma=F_\Sigma E_\Sigma+qK_\Sigma+q^{-1}K_\Sigma^{-1}\).
Its induced action on (15) is
\[
 \mathcal B_m(\Omega_\Sigma)
       =q x^mQ^{-J}+q^{-1}x^{-m}Q^J.
 \tag{21a}
\]
The first term \(F_\Sigma E_\Sigma\) has image in the subspace
being quotiented; the Cartan terms give (21a). Insert any power
\(\Omega_\Sigma^p\) into (9). This is still an analytic actual
degree-preserving total intertwiner, so at the root
\[
 \sum_{j=0}^{rd}w_j\omega_j^p t_j(1)=0\quad(p\ge0),\qquad
 \begin{cases}
 v_j=q^{r+2j},\\
 \omega_j=(-1)^m(v_j+v_j^{-1}),\\
 w_j=(-1)^r(v_j^{-1}-v_j).
 \end{cases}
 \tag{21b}
\]
For this paragraph alone put
\(c_a=\sum_{j\equiv a\ (N)}t_j(1)\), \(a\in\mathbb Z/N\).
Two \(\omega_a\)'s agree exactly when their labels are equal or
are related by \(a^\sharp=-a-r\). On each two-element orbit the
weights \(w_a,w_{a^\sharp}\) are opposite and nonzero; on a
self-orbit they vanish. The Vandermonde matrix on the distinct
\(\omega\)-values is invertible. Taking enough finite powers in
(21b) therefore proves
\[
 c_a=c_{-a-r},\qquad
 T(s,1)\equiv s^{-r}T(s^{-1},1)\pmod{s^N-1}
 \tag{21c}
\]
in the Laurent-polynomial quotient. This is the residue-level
reciprocal-Casimir pairing expressed in the degree variable.
It does not identify individual integer coefficients \(t_j\),
their meridian derivatives, or two geometric contributions.

## 5. The whole-meridian rational reduction

We now distinguish the classical variable \(x_{\rm cl}=-M\) from
the quantum \(x=-M/q\). In this section write \(x=x_{\rm cl}\)
only; no off-root quantum parameter is introduced. Use M's
factorial coordinates
\[
 K_j=x/A_j,\qquad e_j=(M/A_j-M^{-1})p_j,
                         f_j=(1-A_j)/p_j.
 \tag{22}
\]
At resolved zeros their regular rational versions are retained.
The selected inverse-meridian eigenline of
\(G_j=\begin{pmatrix}K_j&e_j\\K_jf_j&K_j^{-1}+e_jf_j\end{pmatrix}\)
is \([p_j:1]\), with eigenvalue \(x^{-1}\); direct multiplication
verifies this also on the resolved chart.

G derives the Euler-star graph from its finite coefficients. Its
recipient prefix action is conjugation by
\(g=\begin{pmatrix}C&p/x\\0&1\end{pmatrix}\), where
\(C=1-pF_{\rm r}/x\). Extend its first resolved head to variable
\(M\) by
\[
 A_1=1+pt,\quad K_1=x/(1+pt),\quad f_1=-t,
                    e_1=(M/(1+pt)-M^{-1})p.
 \tag{23}
\]
Substituting in that same Euler graph gives
\[
 K_{1,\mathrm{old}}=xC/(1+pt),\qquad
 f_{1,\mathrm{old}}=-(t+F_{\rm r}/x)/C,
       \qquad F_{\rm r,old}=F_{\rm r}.
 \tag{24}
\]
Thus the original total lowering coordinate is exactly \(-t\).
This is a variable-meridian calculation; G's root section is not
being differentiated as an unproved whole-meridian identity.

On \(t=0\), set
\[
 H_1^0=\begin{pmatrix}x&0\\-F_{\rm r}&x^{-1}\end{pmatrix},\quad
 h_0=\begin{pmatrix}1&0\\-F_{\rm r}/x&1/x\end{pmatrix},\quad
 U(p)=\begin{pmatrix}1&p\\0&1\end{pmatrix}.
 \tag{25}
\]
The first original meridian from (24) is
\[
 \begin{pmatrix}
 x-pF_{\rm r}&(x^{-1}-x)p+p^2F_{\rm r}\\
 -F_{\rm r}&x^{-1}+pF_{\rm r}
 \end{pmatrix}=U(p)H_1^0U(p)^{-1}.
 \tag{26}
\]
For every later meridian the prefix identity is
\[
 b_{-,1}^{-1}g
  =\begin{pmatrix}C&p/x\\-F_{\rm r}/x&1/x\end{pmatrix}
  =U(p)h_0,
 \qquad h_0^{-1}H_1^0=\operatorname{diag}(x,1).
 \tag{27}
\]
Hence the whole original tuple is \(U(p)H^0U(p)^{-1}\), where
\(H_{j+1}^0=h_0H_j^{\rm r}h_0^{-1}\). If \(K_{\rm r},E_{\rm r},F_{\rm r}\)
are the remaining ordered totals, multiplication gives
\[
 P^0=\begin{pmatrix}xK_{\rm r}&E_{\rm r}\\0&(xK_{\rm r})^{-1}\end{pmatrix},
 \quad K_\Sigma=xK_{\rm r},\quad
 E_\Sigma=E_{\rm r}+p(K_\Sigma^{-1}-K_\Sigma).
 \tag{28}
\]

For completeness, the nontrivial boundary generator still is the
quotient map at variable \(M\). In the section \(p=t=0\), write
\(F_{\rm r}=f_2+K_2^{-1}F_T\). The first original head has
\(K_1=x,e_1=0,f_1=-F_{\rm r}/x\). Substitution in M's positive
crossing formula (4.6), with its denominator \(1-e_1f_2=1\), gives
\[
 K_{1,R}=K_2,\quad K_{2,R}=x,\quad e_{1,R}=e_2/x,\quad e_{2,R}=0,
 \qquad f_{1,R}=xf_2,\quad f_{2,R}=f_R=-xK_2f_2-F_T/x.
 \tag{29}
\]
The first selected flag after this Hurwitz move is
\([p_2/x:1]\): its conjugator on the old second flag is
\((H_1^0)^{-1}h_0=\operatorname{diag}(x^{-1},1)\).
Undoing (27) therefore uses
\[
 p_{1,\mathrm{new}}=p_2/x,\qquad
 g_m=\begin{pmatrix}K_2/x&p_2/x^2\\0&1\end{pmatrix}.
 \tag{30}
\]
Conjugating the old first recipient
\(\begin{pmatrix}x&0\\xf_R&x^{-1}\end{pmatrix}\) by \(g_m^{-1}\)
gives
\[
 K_{2,\mathrm{new}}=x-p_2f_R/x=K_2+p_2F_T/x^2,
                 \qquad p_{2,\mathrm{new}}=-p_2/(xK_2).
 \tag{31}
\]
The equality uses only \(p_2f_2=1-x/K_2\). The flag computation,
unlike division by \(e_2\), remains valid at a resolved zero.
Equation (31) is precisely the diagonal map
\(p_2\mapsto-A_2p_2/x^2\), followed by the remaining Euler star.

The later heads agree as well. Put \(K'=K_{2,\mathrm{new}}\),
\(C_T=K'/K_2\), and define
\[
 g_T=\begin{pmatrix}C_T&-p_2/(x^2K_2)\\0&1\end{pmatrix},\quad
 b_{-,\mathrm{new}}=\begin{pmatrix}1&0\\-K_2f_R&K'\end{pmatrix},\quad
 b_{-,R}=\begin{pmatrix}1&0\\-xf_R&x\end{pmatrix}.
 \tag{32}
\]
Direct multiplication, using (31), gives
\[
 g_T^{-1}b_{-,\mathrm{new}}=b_{-,R}g_m
       =\begin{pmatrix}K_2/x&p_2/x^2\\-K_2f_R&K'\end{pmatrix}.
 \tag{33}
\]
Ratios of these prefix identities identify every later dressed
meridian. Internal crossings preserve the remaining totals and
commute with (24)--(27); their quotient is the same physical
crossing. Inverses follow by rational inversion. We have proved
the full whole-meridian reduced word graph, not only its first
entry. None of (23)--(33) used \(x^2=1\).

All these equations hold where the displayed Gauss denominators
are units, with resolved coordinates at the specified zeros.
They are identities of rational charts over local Artin rings.
They assert a canonical correspondence from the actual finite
local coefficients, not a uniform asymptotic kernel theorem.

## 6. The degree twist is the marked axis multiplier

For \(s\ne0\), the degree twist has the exact diagonal canonical
map \(A_j\mapsto A_j,\ p_j\mapsto sp_j\). Denote it by
\(\mathcal D_s\). In (22) this keeps \(K_j\) fixed and sends
\(e_j\mapsto se_j,\ f_j\mapsto s^{-1}f_j\). Therefore it
conjugates all remaining dressed meridians by
\(D(s)=\operatorname{diag}(s,1)\). Equations (25)--(27) show that
it conjugates the entire original section tuple by the same
matrix, including its first head.

The rational fixed scheme relevant to the trace of
\(s^J\mathcal B_m(W_\beta)\) is
\[
                   \mathcal D_s\circ R_{\beta,\mathrm{red}}(z)=z.
 \tag{34}
\]
Here \(R_{\beta,\mathrm{red}}\) is the physical point-map
convention just proved. Write the selected total as
\(P=\begin{pmatrix}k&E_\Sigma\\0&k^{-1}\end{pmatrix}\), with
\(k-k^{-1}\) a unit. Lifting (34) through the upper-unipotent
quotient (26) gives
\[
 R_{\beta,\mathrm{pt}}(H^0)=C_{\rm pt}H^0C_{\rm pt}^{-1},\qquad
 C_{\rm pt}=U(u)D(s)^{-1}
            =\begin{pmatrix}s^{-1}&u\\0&1\end{pmatrix}.
 \tag{35}
\]
Preservation of \(P\) determines the missing upper entry uniquely:
\[
               u=\frac{(s^{-1}-1)E_\Sigma}{k-k^{-1}}.
 \tag{36}
\]
Conversely this centralizing matrix recovers precisely (34).
The ratio of its eigenvalues on the selected \(k\) and \(k^{-1}\)
lines is \(s^{-1}\).

B defines the marked multiplier \(z_\beta\) in the observable
inverse-Hurwitz convention. That convention is inverse to the
physical point map: for one positive crossing its tuple rule is
\((H_i,H_{i+1})\mapsto(H_{i+1},H_{i+1}H_iH_{i+1}^{-1})\).
For a signed word \(W=R_\ell\cdots R_1\), the physical map is
\(R_{\ell,\mathrm{pt}}\circ\cdots\circ R_{1,\mathrm{pt}}\).
Substitution of the coordinate matrices in \(\operatorname{Ad}_W\)
has the reverse order \(\beta_1\circ\cdots\circ\beta_\ell\),
where \(\beta_i=R_{i,\mathrm{pt}}^{-1}\). It is therefore the
inverse map for the whole mixed word, not just one crossing.
Equivariance under simultaneous conjugation makes its closing
conjugator the inverse of (35). Denote B's regular, selected-total
character-fixed germ by \(\mathcal Y_\beta\). Then
\[
 \boxed{\quad
 \operatorname{Fix}(\mathcal D_s\circ R_{\beta,\mathrm{red}})
       /\mathbb G_m
       \simeq \{z_\beta=s\}\subset\mathcal Y_\beta.
 \quad}\tag{37}
\]
This includes nilpotent directions: B's conjugator line and its
eigenvalue ratio are defined over local Artin rings, and (36)
uses a unit denominator. In the reverse direction, normalize
the physical conjugator's second diagonal entry to one. Its
ratio \(s^{-1}\) and commutation with \(P\) force exactly
(35)--(36). This proves both directions as schemes.

One common diagonal framing still has to be quotiented.
Locally choose the total \(k\)-eigenline as the first coordinate
line and the first meridian's selected inverse eigenline as the
second. They are assumed distinct. This puts the original tuple
in (25), uniquely up to common diagonal conjugation; M's Gauss
inverse reconstructs all remaining coordinates. Near G's regular
complete geometric tuple these choices and the required unit
denominators persist. Quotienting this remaining diagonal action
therefore identifies (37) with B's character-fixed axis germ.
It is not discarded as if (34) already had an isolated point.
In particular \(\mathcal D_s\) itself becomes trivial as a map
after character reduction: it is common conjugation. The value
\(z_\beta=s\) is detected by its equivariant fixed-point lift
before that quotient, not by a nontrivial scaling action on the
character quotient.

If, in addition, the original exterior is supplied with the
positive complete gluing certificate in G and the resulting
fixed-meridian literal germ is the reduced point required in A,
then A proves that this character-fixed germ is a smooth surface
with coordinates \((\mu,z_\beta-1)\). By (37), near \(s=1\) these
are equivalently \((\mu,\log s)\). This conditional smoothness
does not require the selected total eigenvalue \(k\) to have a
nonzero derivative along the axis curve. The meridian eigenvalue,
not its parabolic trace, is the parameter \(\mu\).
Our selected inverse-meridian flag corresponds to A's opposite
choice by the analytic coordinate change \(\mu\mapsto-\mu\).
This does not change the fixed-root germ or its smoothness, and
does not change the original derivative convention in (7)--(10).

On an already regular marked logarithmic generating chart, the
degree twist contributes \((\log s)\sum_j\Log A_j\). Its conjugate
moment is therefore the retained sum \(\sum_j\Log A_j\), equal
to \(m\Log x_{\rm cl}-\Log k\) with its actual integer logarithmic
offset. This observation does not supply a holomorphic primitive
at a factorial boundary or identify the quantum \(\mu\)-normal
with differentiation in \(\log s\).

## 7. An exact residue constraint on a hypothetical single branch

The root identity (9) imposes a concrete limitation on an asymptotic
interpretation of this family. Put \(h=\log Q=2\pi i/N\) and
\(\eta=\log s\). Suppose, conditionally, that on a fixed complex
neighborhood of \(\eta=0\) the unmarked root polynomial had the
single uniform form
\[
 T_{\beta,N}(e^\eta,1)
       =b_N e^{S(\eta)/h}\bigl(A(\eta)+o(1)\bigr),
 \qquad b_N\ne0,\quad A(0)\ne0,
 \tag{38}
\]
where \(S,A\) are holomorphic and the error is uniform. The scalar
\(b_N\) may retain the original \(N\)-dependent normalization.
Evaluating at \(\eta=\pm h\), dividing (9) by
\(b_Ne^{S(0)/h}A(0)\), and using Taylor's formula gives
\[
 c_\infty e^{-S'(0)}-c_\infty^{-1}e^{S'(0)}=0,
                   \qquad c_\infty=(-1)^r.
 \tag{39}
\]
No source estimate was used in this implication.

If the branch in (38) had the geometric moment calibrated at the
end of Section 6, then
\(e^{S'(0)}=x_{\rm cl}^{m}/k\), with \(x_{\rm cl}=-1\).
The left side of (39) would be
\[
                       -(k-k^{-1}),
 \tag{40}
\]
which is a unit at the regular total product. Thus an unopposed
nonzero root packet of the form (38) with that slope is impossible.
This does not exclude a meridian family whose leading root
amplitude vanishes but whose first meridian coefficient survives,
equal-action contributions that cancel in (9), or other retained
contour terms. Those possibilities cannot be removed when using
the original first-jet filling (10).

## 8. What is and is not assembled

The same finite polynomial now has an exact original filling
functional, an uncollapsed integer-degree full-twist action, and a
rational axis fixed-scheme interpretation. The proof retains the
whole meridian, finite caps, marked loops and outside source lines.
Its nonzero extreme coefficients do not force a geometric
coefficient. In particular (37) identifies equations of a rational
correspondence; it is not a contour deformation for (4), nor an
estimate of its saddle contributions. The prescribed root filling
still uses the cancellation and first jet in (9)--(10), rather
than a value at an arbitrarily chosen classical axis point.

No positivity, surviving geometric cycle, or lower bound for the
original source is proved. No additional volume-conjecture case
or finite-exception conclusion is asserted.

## Complete proof-source pins

* R: notes/research_actual_reduced_braid_source.md, 330 lines,
  SHA256 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* W: notes/research_actual_full_twist_highest_multiplicities.md, 453 lines,
  SHA256 2014de44e1ab880c61c6d1017d6f6a4bf3ed18cd6065e1fcf1fe84d1c8e7090f.
* G: notes/research_actual_reduced_braid_critical_scheme.md, 564 lines,
  SHA256 ddddcd9bf75f35afdf3e5de0c03323acee2c66e624db36142c2344ef729a977a.
* M: notes/marked_braid_holonomy.md, 529 lines,
  SHA256 eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.
* B: notes/research_braid_axis_closure_multiplier.md, 510 lines,
  SHA256 0c473ffed9a15cc8193b73a0323cd9058986e56dfc47731470a72ac764be34e0.
* A: notes/research_braid_axis_transverse_filling_germ.md, 306 lines,
  SHA256 a1689bf264ec6ba315ec10d70efdad763f7309ac1856c4617c4f85870f467dc3.

All six complete directs were freshly read nontruncated in this
active author sequence, and every used implication was checked.
Only written mathematics and text/hash operations were used.
Frozen and public files were not changed.
