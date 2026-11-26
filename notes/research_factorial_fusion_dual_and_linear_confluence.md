# Factorial fusion duals and linear confluence depth for the original source

Written research proof, 22 November 2026.

An exact contravariant dual to the generic Clebsch inclusion has a short
factorial formula. Cancelling two Gaussian ratios shows that every raw
inclusion term has pole order at most one and every raw dual term at most
two. For \(b\) physical strands this gives source-frame jet depth
\(3(b-1)\), independently of the level and the length of the physical
braid word. It sharpens the coarser projector bound in [U].

The same formulas supply the controlled inverse expressions required by
the factorial-envelope theorem [E]. Applied to one complete ambient-word
contraction, they give an upper envelope for the original marked root
scalar. All leaf gauges cancel before absolute values are taken. This
does not supply a sharp geometric envelope or a scalar lower bound.

## 1. Conventions and statement

Fix \(N\ge2\), \(d=N-1\), an even width \(b\ge2\), and
\[
 q_0=e^{\pi i/N},\qquad u=\zeta-q_0,\qquad
 \mathcal O=\mathbb C\{u\},\qquad
 \mathcal K=\operatorname{Frac}\mathcal O,\qquad
 \rho=\zeta-\zeta^{-1},\qquad
 [n]=\frac{\zeta^n-\zeta^{-n}}{\rho}.
 \tag{1}
\]
Put \([0]!=1\), \([n]!=\prod_{a=1}^n[a]\), and
\(\binom nr_\zeta=[n]!/([r]![n-r]!)\) for \(0\le r\le n\).
Every half-integral power of \(\zeta\) uses the fixed local logarithm.
Valuations below refer to \(u=0\). In particular
\[
 \nu([n]!)=\lfloor n/N\rfloor,\qquad
 \nu\binom nr_\zeta
 =\lfloor n/N\rfloor-\lfloor r/N\rfloor
                    -\lfloor(n-r)/N\rfloor\in\{0,1\}.
 \tag{2}
\]
Indeed each quantum integer of nonzero index divisible by \(N\) has a
simple zero and \(\rho(q_0)\ne0\). No prime-level assumption is involved.

Use the actual balanced physical leaf family of [S,U]. Let
\[
 \mathcal M_{\mathcal O}=V_d(\zeta)^{\otimes b},\qquad
 \mathcal I_{\mathcal K}
   =\operatorname{Inv}_{\mathcal K}(\mathcal M_{\mathcal O}\otimes\mathcal K),
 \qquad
 \Lambda=\mathcal I_{\mathcal K}\cap\mathcal M_{\mathcal O},\qquad
 \mathcal V=\Lambda/u\Lambda.
 \tag{3}
\]
The last space embeds in the physical root tensor because \(\Lambda\)
is saturated. It contains every state obtained from the regular original
cup source by the regular original gates [S,U]. It need not be the entire
root invariant space [M].

**Theorem.** For each binary fusion tree \(T\), with all \(b\) leaves
labelled \(d\), root label zero, and all admissible internal colors
retained, the explicit inclusions and duals below give matrices \(B_T,L_T\)
with
\[
 \operatorname{im}B_T=\mathcal I_{\mathcal K},\qquad L_TB_T=I,\qquad
 u^pB_T,\ u^qL_T\ \text{regular},\qquad
 p=b-1,\quad q=2(b-1),\quad m=p+q=3(b-1).
 \tag{4}
\]
These bounds hold term by term in the specified finite formulas.
The intrinsic coordinate lattice \(\Lambda_T=B_T^{-1}\Lambda\) satisfies
\[
 u^p\mathcal O^g\subset\Lambda_T\subset u^{-q}\mathcal O^g,
 \qquad g=\dim_{\mathcal K}\mathcal I_{\mathcal K}.
 \tag{5}
\]
Set \(\mathcal C_T=u^pB_T\). Then the exact root source is
\[
 \boxed{\quad
 \mathcal V=
 \left\{[u^m](\mathcal C_Tz):
 \begin{array}{l}
 z\in(\mathcal O/u^{m+1})^g,\\
 [u^j](\mathcal C_Tz)=0\quad(0\le j<m)
 \end{array}\right\}.
 \quad}
 \tag{6}
\]
Only Laurent coefficients of \(B_T\) at orders \(-p,\ldots,q\) occur.
For every whole regular physical word \(W\),
\[
                    \nu(L_{T'}WB_T)\ge-m.
 \tag{7}
\]
The source-frame depth and (7) are independent of word length. The
number of coordinates is still allowed to grow with \(N\).

For any fixed physical braid word, the explicit formulas also give a
polynomial-in-\(N\) factorial upper envelope for its original marked
root scalar, as specified in section 7. Constants in that analytic
upper bound may depend on the fixed word and filling powers.

## 2. The inclusion, with one possible pole per raw term

In the divided-\(F\) basis \(v_j^{(A)}=F^jv_0^{(A)}/[j]!\), use
\[
 Fv_j=[j+1]v_{j+1},\qquad Ev_j=[A-j+1]v_{j-1},\qquad
 Kv_j=\zeta^{A-2j}v_j,
 \qquad
 \Delta E=E\otimes K+I\otimes E,\quad
 \Delta F=F\otimes I+K^{-1}\otimes F.
 \tag{8}
\]
Endpoint arrows outside \(0,\ldots,A\) are zero. For
\(C=A+B-2k\), \(0\le k\le\min(A,B)\), normalize the highest vector by
\[
 h_C=\sum_{r=0}^k b_r\,v_r^{(A)}\otimes v_{k-r}^{(B)},\qquad
 b_r=(-1)^r\zeta^{r(2k-B-r-1)}
       \frac{[B-k+r]![A-r]!}{[B-k]![A]!}
   =(-1)^r\zeta^{r(2k-B-r-1)}
       \frac{\binom{B-k+r}{r}_\zeta}{\binom Ar_\zeta}.
 \tag{9}
\]
The equation \(\Delta E\,h_C=0\) gives
\(b_{r+1}/b_r=-\zeta^{-B+2k-2r-2}[B-k+r+1]/[A-r]\), so \(b_0=1\)
fixes every phase. Define
\(\iota_Cv_n=(\Delta F)^nh_C/[n]!\).
Its output coefficient at \((i,w)\), where \(i+w=k+n\), is exactly
\[
 I_C(i,w;n)=
 \sum_r b_r\,
       \zeta^{(n-i+r)(i+r-A)}
       \binom ir_\zeta\binom w{k-r}_\zeta .
 \tag{10}
\]
The sum retains precisely the indices
\(0\le r\le k\), \(0\le i-r\le n\), with
\(0\le i\le A\), \(0\le w\le B\). To verify it, the divided coproduct is
\[
 \frac{(\Delta F)^n}{[n]!}
   =\sum_{s=0}^n\zeta^{-s(n-s)}
                K_1^{-s}F_1^{(n-s)}\otimes F_2^{(s)},
 \qquad F^{(a)}=F^a/[a]!.
 \tag{11}
\]
This follows by induction from \(FK^{-1}=\zeta^{-2}K^{-1}F\).
On \(v_r\otimes v_{k-r}\), put \(s=n-i+r\) to obtain (10).
Formula (2) now gives valuation at least \(-1\) for each raw summand:
the two descendant Gaussians are regular, and (9) has only one
Gaussian in its denominator.

For completeness, \(EF^jh_C=[j][C-j+1]F^{j-1}h_C\) proves nonvanishing
through \(j=C\). A nonzero \(F^{C+1}h_C\) would be highest of negative
weight \(-C-2\), with a nonterminating \(F\)-string, impossible in this
finite tensor. Thus \(\iota_C\) is defined on all \(V_C\). Its Casimir
\(\Omega=\rho^2FE+\zeta K+\zeta^{-1}K^{-1}\) has distinct generic
eigenvalues \(\zeta^{C+1}+\zeta^{-C-1}\); the dimension identity
\(\sum_k(A+B-2k+1)=(A+1)(B+1)\) proves generic completeness [U].

## 3. An exact bilinear norm and its finite Vandermonde proof

Define the diagonal **bilinear**, not Hermitian, pair form
\[
 G_{A,B}(i,j)=
       \zeta^{Bi+Aj-2ij}\binom Ai_\zeta\binom Bj_\zeta,\qquad
 G_C(n)=\binom Cn_\zeta.
 \tag{12}
\]
Its neighboring diagonal ratios show directly that \(\Delta F\) and
\(\Delta E\) are adjoints:
\[
 \frac{G(i+1,j)}{G(i,j)}
    =\zeta^{B-2j}\frac{[A-i]}{[i+1]},\qquad
 \frac{G(i,j+1)}{G(i,j)}
    =\zeta^{A-2i}\frac{[B-j]}{[j+1]}.
 \tag{13}
\]
Here and below transposes are ordinary transposes. The Casimir is
self-adjoint for this form, hence distinct generic channels are
orthogonal. Their highest norm is
\[
 \theta_{A,B,k}=\langle h_C,h_C\rangle_G
 =\zeta^{k(A-B+k-1)}
   \frac{[B]![A-k]![A+B-k+1]!}
        {[B-k]![A]![k]![C+1]!}
 =\zeta^{k(A-B+k-1)}
   \frac{\binom Bk_\zeta\binom{C+k+1}k_\zeta}{\binom Ak_\zeta}.
 \tag{14}
\]
Here is an elementary proof of the sum, including its normalization.
Put \(Y=B-k\). Substitution in (9),(12) gives
\[
 b_r^2G(r,k-r)
 =\zeta^{Ak-r(C+2)}
       \frac{[B]!}{[Y]!^2[A]!}
       \frac{[Y+r]![A-r]!}{[r]![k-r]!}.
 \tag{15}
\]
It remains to evaluate
\[
 \sum_{r=0}^k \zeta^{-r(C+2)}
          \binom{Y+r}r_\zeta\binom{A-r}{k-r}_\zeta
       =\zeta^{-k(Y+1)}\binom{A+Y+1}k_\zeta.
 \tag{16}
\]
For \(Q=\zeta^2\),
\(\binom ab_\zeta=\zeta^{-b(a-b)}{a\brack b}_Q\).
Cancelling the common powers converts (16) to
\[
 \sum_{r=0}^kQ^{-r(Y+1)}
       {Y+r\brack r}_Q{A-r\brack k-r}_Q
       =Q^{-k(Y+1)}{A+Y+1\brack k}_Q.
 \tag{17}
\]
Multiply by \(Q^{k(Y+1)}\) and set \(j=k-r\). This is the coefficient
of \(z^k\) in the exact formal identity
\[
 \frac{1}{(z;Q)_{Y+1}(Q^{Y+1}z;Q)_{A-k+1}}
             =\frac{1}{(z;Q)_{A+Y-k+2}}.
 \tag{18}
\]
Indeed \(\sum_{n\ge0}{a+n\brack n}_Qz^n=(z;Q)_{a+1}^{-1}\)
follows by induction from the finite product and the Gaussian Pascal
identity. Only a finite coefficient is used. Equations (15)--(16)
give (14), since \(Ak-k(Y+1)=k(A-B+k-1)\).

Using adjointness and
\(E^nv_n=[C]!/[C-n]!\,v_0\) now gives
\[
 \iota_C^tG_{A,B}\iota_C=\theta_{A,B,k}G_C,\qquad
 \pi_C=\theta_{A,B,k}^{-1}G_C^{-1}\iota_C^tG_{A,B},\qquad
 \pi_C\iota_D=\delta_{CD}I,\quad \sum_C\iota_C\pi_C=I.
 \tag{19}
\]
The dual is therefore the same literal generic projection as in [U],
rather than an unspecified inverse matrix. Neither \(G\) nor its
root specialization is asserted positive.

## 4. Two cancellations in each raw dual coefficient

For \(i+w=k+n\), the \((n;i,w)\) entry of \(\pi_C\) is
\(I_C(i,w;n)G_{A,B}(i,w)/
(\theta_{A,B,k}\binom Cn_\zeta)\).
In each summand of (10) use the two exact Gaussian identities
\[
 \frac{\binom Ai_\zeta\binom ir_\zeta}{\binom Ar_\zeta}
       =\binom{A-r}{i-r}_\zeta,\qquad
 \frac{\binom Bw_\zeta\binom w{k-r}_\zeta
                    \binom{B-k+r}r_\zeta}{\binom Bk_\zeta}
       =\binom kr_\zeta\binom{B-k+r}{w-k+r}_\zeta.
 \tag{20}
\]
They follow by cancelling factorials; all indices on the right are
valid because \(w-k+r=n-i+r\) is an allowed descendant index.
Consequently the raw dual summand is exactly
\[
 (-1)^r\zeta^{\Psi(i,w,n,r)}
 \frac{\binom Ak_\zeta\binom kr_\zeta
       \binom{A-r}{i-r}_\zeta\binom{B-k+r}{w-k+r}_\zeta}
      {\binom{C+k+1}k_\zeta\binom Cn_\zeta},
 \tag{21}
\]
where
\[
 \Psi=r(2k-B-r-1)+(n-i+r)(i+r-A)
                  +Bi+Aw-2iw-k(A-B+k-1).
 \tag{22}
\]
Thus every numerator is Laurent regular, and each of the two
denominator Gaussians has valuation at most one. Each raw dual
summand has pole at most two. This is stronger than bounding the
uncancelled inclusion, \(G\), \(\theta^{-1}\), and \(G_C^{-1}\)
separately. All equalities were proved over \(\mathcal K\); at root
zeros they mean the corresponding complete Laurent germs.

Each summand in (10),(21) has a fixed number of factorials, with
arguments \(O_b(N)\), phase exponent \(O_b(N^2)\), and a number of
indices bounded in terms of width. These also enter the analytic bound.

## 5. Tree frames and the finite source equations

Compose the inclusions from the root \(V_0\) to the leaves, retaining
every admissible internal color, to form \(B_T\). Compose (19) in
reverse order to form \(L_T\). Completeness proves \(L_TB_T=I\) and
\(\operatorname{im}B_T=\mathcal I_{\mathcal K}\).
A binary \(b\)-leaf tree has \(b-1\) vertices. Expanding its finite
formulas gives raw pole bounds \(p=b-1\) and \(q=2(b-1)\); sums cannot
worsen them.

The external change to the actual balanced leaf frame is literal:
\[
 w_a=s_av_a^{(d)},\qquad
 s_a=(-\rho)^{-a}\zeta^{-a(a+1)/2},\qquad
 B_T^{\rm bal}=D^{-1}B_T^{\rm div},\quad
 L_T^{\rm bal}=L_T^{\rm div}D,\quad D=\bigotimes_{\text{leaves}}\operatorname{diag}s_a.
 \tag{23}
\]
This is exactly [U]'s gauge for [S]'s actual generic family. It and
its inverse are DVR units, so the pole estimates are unchanged.
Their analytic norms have not been bounded.

For \(x\in\mathcal O^g\), \(u^pB_Tx\in\Lambda\); conversely, if
\(B_Tx=\psi\in\Lambda\), then \(x=L_T\psi\in u^{-q}\mathcal O^g\).
This proves (5). For the finite formula (6), given \(\psi\in\Lambda\)
put \(z=u^qL_T\psi\). Then
\[
                         \mathcal C_Tz=u^{p+q}\psi.
 \tag{24}
\]
Its \(m\)-jet gives the required root vector. Conversely a polynomial
representative \(z\) satisfying (6) gives the regular vector
\(\psi=u^{-m}\mathcal C_Tz\). It is generically invariant, hence
belongs to \(\Lambda\), and has the stated root. Both directions use
only \(\mathcal C_T\bmod u^{m+1}\), proving the advertised Laurent range.

Independent root vectors from (6) have lifts forming an \(\mathcal O\)
basis of \(\Lambda\). The original physical word preserves both generic
invariants and the ambient lattice [S,U], hence \(\Lambda\); (4) proves
(7). Intrinsic lattice changes of tree are unimodular.

There is a constructive minimization consequence. Let \(Z_T\) be the
kernel of the lower-coefficient map \(z\mapsto([u^j]\mathcal C_Tz)_{j<m}\)
on finite jets, and let \(E_Tz=[u^m]\mathcal C_Tz\). Then
\(E_T(Z_T)=\mathcal V\), of dimension \(g\), so
\(Z_T/\ker(E_T|_{Z_T})\simeq\mathcal V\). Any minimization in which this
block enters only through the physical root state may eliminate that
kernel before forming its positive Gram. This removes redundant jet
variables, but gives neither a smaller source than \(\mathcal V\) nor
a bound on the conditioning of the elimination or the resulting Gram.

For root-value computation, the physical action is the restriction of
\(W(q_0)\) to the space (6). Thus positive-order word jets are not
required merely because the fusion frame has poles. Independently
prescribed quantum-normal or main-color derivatives still require
their own differentiated operators and co-source; a root row does
not determine those germs.

## 6. Ambient crossing terms and the full marked closing

Here the word is fixed before \(N\) tends to infinity. Its generators
are the original signed physical crossings, with the actual Cartan,
framing, cup and cap conventions [S,M,B]. In the divided leaf basis
the unbraided positive finite universal matrix has the form
\[
 \mathcal R^+
 =\zeta^{H\otimes H/2}
   \sum_{n=0}^{d}
       \frac{\zeta^{n(n-1)/2}\rho^n}{[n]!}E^n\otimes F^n .
 \tag{25}
\]
The coefficient recurrence \(c_{n+1}/c_n=\zeta^n\rho/[n+1]\) verifies
intertwining directly. On the checked channel \(C=2d-2k\), its
zero-transfer term and (9)'s endpoint \(b_k\) give the scalar
\((-1)^k\zeta^{d^2/2-k(2d+1-k)}\), exactly [B]'s generic crossing.
Generic completeness therefore identifies the matrix, including its
Cartan scalar. The prescribed swaps or self-dual convention are retained.
For example its term from \((i,j)\) to \((i-n,j+n)\) has a Cartan
monomial times
\[
       \rho^n\frac{[d-i+n]![j+n]!}
                         {[d-i]![j]![n]!},
       \qquad 0\le n\le\min(i,d-j).
 \tag{26}
\]
Every factorial index is below \(N\). The inverse is the same finite
type: invert the Cartan factor and replace the series coefficient by
\((-1)^n\zeta^{-n(n-1)/2}\rho^n/[n]!\). The finite Gaussian binomial
identity verifies the inverse series, as \(E\otimes F\) is nilpotent.
Thus each raw ambient crossing term is regular at \(q_0\), including
negative crossings. No root spectral derivative is deleted.

Write \(b=2k\), \(D_0=kd\), and let \(\mathbf p(\zeta)\) be the tensor
of \(k\) regular original generic cups from [S]. With \(x=\zeta^d\),
their nonzero coefficients are
\[
 p_a=Nx^{-d}(-x)^a(\zeta^2)^{-a(a+1)/2}
       \frac{F_aF_{d-a}}{F_d},\qquad
 F_n=\prod_{j=1}^n(1-\zeta^{2j}),\qquad (a,d-a).
 \tag{27}
\]
All denominators are units at \(q_0\). They are generic invariants and
specialize to the original cups. Choose any regular row lift of the
original ordinary and marked caps that retains the ordinary degree
supports. One explicit choice is
\[
 \ell_{a,b'}(\zeta)=\frac{x^{-a}\zeta^{-2a}}N\,
                          \delta_{a+b',d},\qquad
 m_{a,b'}(\zeta)=\frac{x^{b'}}{N^2},\qquad
 \lambda(\zeta)=\ell(\zeta)^{\otimes(k-1)}\otimes m(\zeta).
 \tag{28}
\]
At \(q_0\) these are [M]'s full rows. This auxiliary lift need not
satisfy \(m(\zeta)p(\zeta)=1\) or define a prescribed generic Jones/ADO
family; only its original root value is used.

Every generic invariant and \(\mathbf p\) has total physical degree
\(D_0\), and \(W\) preserves this integer degree. In the full closing,
the first \(k-1\) ordinary caps require degree \((k-1)d\); only then is
the last marked pair restricted to degree \(d\). The marked row in
(28) has not been independently degree-truncated on arbitrary inputs.
Keeping the original external scalar \(\chi_N\) outside, the root
invariant is exactly
\[
 K_N=\chi_N\,\mathcal F_N(q_0),\qquad
 \mathcal F_N(\zeta)=
       \lambda^{\rm bal}W^{\rm bal}
             B_T^{\rm bal}L_T^{\rm bal}\mathbf p^{\rm bal}
       =\lambda^{\rm bal}W^{\rm bal}\mathbf p^{\rm bal}.
 \tag{29}
\]
Expanding \(W\) in original ambient matrices (25), inside this single
frame identity, gives raw pole at most \(m\). A summed transport pole
bound alone would not justify this termwise conclusion.

The potentially large leaf gauge cancels *before* estimation.
On the degree-\(D_0\) sector write
\[
 D=(-\rho)^{-D_0}Z,\qquad
 Z_{\mathbf a}=\zeta^{-\sum_j a_j(a_j+1)/2},\qquad
 \widehat{\mathbf p}=Z\mathbf p^{\rm bal},\qquad
 \widehat\lambda=\lambda^{\rm bal}Z^{-1}.
 \tag{30}
\]
Since \(W^{\rm bal}=D^{-1}W^{\rm div}D\), the exact same scalar is
\[
          \mathcal F_N=
              \widehat\lambda W^{\rm div}
                         B_T^{\rm div}L_T^{\rm div}\widehat{\mathbf p}.
 \tag{31}
\]
The powers \((-\rho)^{D_0}\) and \((-\rho)^{-D_0}\) have cancelled.
All remaining gauges are the explicitly retained monomials \(Z\);
no assertion about the norm of \(D\) has been used.

## 7. The explicit factorial upper envelope, including confluence

The symmetric factorial conversion is
\[
                 [a]!=(-1)^a\zeta^{-a(a+1)/2}\rho^{-a}F_a.
 \tag{32}
\]
Each Gaussian in (9)--(22) has zero net factorial-index balance.
In (26) the net factorial index is \(n\), so its \(\rho^{-n}\)
is cancelled by the displayed \(\rho^n\). The cups (27) have zero
net index as well. Equations (30)--(31) have already cancelled the
remaining leaf powers of \(\rho\). The rows (28) and all remaining
factors are monomials and powers of \(N\).

Consequently expanding the *one-frame ambient-word expression* (31)
gives polynomially many explicit terms
\[
 \mathcal F_N(\zeta)=\sum_\nu a_{\nu,N}\,
       \zeta^{\beta_{\nu,N}}
          \prod_{a=1}^{J_\nu}F_{n_{\nu,a}}^{\,\epsilon_{\nu,a}},
 \quad
 |a_{\nu,N}|\le C_WN^{A_W},\quad
 |\beta_{\nu,N}|\le A_WN^2,\quad
 J_\nu,|\epsilon_{\nu,a}|\le A_W,\quad
 n_{\nu,a}\le C_bN.
 \tag{33}
\]
Half-integral exponents retain their analytic mark. There are at most
\(C_WN^{A_W}\) terms, since width and the word are fixed and every
physical, channel, or descendant index has \(O_b(N)\) possibilities.
Every raw term has valuation at least \(-m\). The coefficients
\(a_{\nu,N}\) include the literal powers of \(N\) and signs; the exact
Cartan and twist phases remain in \(\beta_{\nu,N}\).

Put \(S_r=\prod_{j=1}^r2\sin(\pi j/N)\), \(S_0=1\). Applying [E] to
each actual term, with root zeros removed before differentiation,
gives constants depending on the fixed width and word such that
\[
 \boxed{\quad
 |K_N|\le |\chi_N|\,C_WN^{B_W}
       \sum_\nu
          \prod_{a=1}^{J_\nu}
                   S_{\,n_{\nu,a}\bmod N}^{\,\epsilon_{\nu,a}} .
 \quad}
 \tag{34}
\]
This is an envelope of the stated literal expansion, not the claim
that all expansions give the same sharp rate.

To spell out the bounded-jet use of [E], take
\(\zeta=q_0e^{h/N}\). A raw term of valuation \(-s\), \(0\le s\le m\),
has constant Laurent coefficient equal to the \(s\)-th Taylor
coefficient of its zero-removed regular part. In [E]'s notation
\(n=aN+r\), the exact leading magnitude of \(h^{-a}F_n\) is
\(2^aa!N^aS_r\). On a disk \(|h|\le c_b/N\), the normalized regular
factor and its inverse have polynomial bounds. Cauchy's estimate
therefore adds only a polynomial cost for these at most \(m\)
derivatives. A term with positive valuation contributes zero to
the constant coefficient. The same argument applies to any
specified fixed set of Laurent coefficients; higher specified orders
add a fixed number of derivatives. It does not identify such an
auxiliary row-lift germ with an independently prescribed marked
quantum-normal family.

The passage between \(h\) and \(u\) changes fixed Laurent coefficients
by polynomial factors only [E]. Half-integral Cartan powers cause no
new issue: their marked normalized value varies by a bounded factor
on this disk since \(|\beta_{\nu,N}|=O_W(N^2)\).
Finally
\[
 \log S_r=N\int_0^{r/N}\log(2\sin\pi t)\,dt+O(\log N)
 \tag{35}
\]
uniformly for every residue \(0\le r<N\). Thus bounded confluence does
not add an unrecorded exponential rate to this explicit positive
factorial envelope. Its maximization need not produce filled volume,
and cancellation may make (34) very far from equality.

There are two distinct quantifiers. The source-frame jet budget
\(m=3(b-1)\) and the whole summed pole bound (7) are independent of
word length. The polynomial exponent, the number of factorials per
term, and constants in (33)--(34) can depend on the chosen fixed word
and its filling powers. Expanding many intermediate fusion changes
can introduce extra apparent termwise poles; no width-only derivative
budget for that different raw expansion is asserted.

## Complete proof sources and limits

All five complete proof texts were read at renewed matching pins.

| Label | Complete source | SHA-256 |
|---|---|---|
| U | [Uniform fusion confluence, 439 lines](research_uniform_fusion_confluence_source.md) | c39b8eaab1e1b4fcd1cdf7bc034a5a4419a33d40e058c2b6d6d06f8096414864 |
| E | [Bounded normal factorial envelope, 162 lines](bounded_normal_quantum_factorial_envelope.md) | 17fbb46d17b9678e35b9800e1c67cca24f846e8b5ccbcc540d360ec3189e1b18 |
| S | [Actual deformable source, 327 lines](actual_six_port_deformable_source_and_recoupling.md) | e29acfe75fb61cead48a08691037d6b81041bb5115b6578c9d2b563c8664c049 |
| M | [Complete original source and caps, 602 lines](actual_complete_source_multiplicity_module.md) | 14cfb558f50c5b091cec9439692dfeb87129e31f38588cb1ebfd8e8547ac99a9 |
| B | [Actual Casimir braiding conventions, 448 lines](casimir_braiding_and_recoupling_lattice.md) | 91e646b893a45e387d301d23fc115c328aa987c3889c726bc70ebcd4db10e54e |

The saturated source, its distinction from the larger root Hom space,
and its exact original closing are existing coverage [U,S,M].
Generic fusion, contravariant forms, and finite Vandermonde identities
are established methods. The refinement here is the explicit cancelled
factorial dual, its raw two-pole bound, the resulting linear confluence
depth, and the controlled factorial upper bound for the full marked
root source. No novelty is claimed for generic recoupling itself.

Every root Hermite direction required by the original source is kept
through (6); no separate eigenprojector is specialized and no positive
fusion quotient is imposed. The bilinear form does not give a tame
Hermitian Gram or a tame Smith inverse. The result neither repairs a
different formal cyclic pentagon nor selects a geometric period.
The external \(\chi_N\) has not been bounded or normalized away.
No original scalar lower estimate, nonzero geometric coefficient,
or finite-exception theorem follows from the upper envelope.

Only written mathematics, text inspection, and hashes were used.
No program, numerical experiment, test, build, git action, or edit
of an earlier final proof was performed.
