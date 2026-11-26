# A nonzero complex amplitude for the complete outgoing polynomial

Private finite-source theorem, 9 November 2026. The terminating outgoing
recurrence determines a nonzero leading amplitude, not only its
exponential rate. A first correction to its stable Riccati solution is
uniform through the last physical row. Multiplication from the exact
value at that row then fixes the complex normalization and both
half-input parity factors.

All statements concern the original complete outgoing polynomial.
They do not estimate its signed pairing with the inner periods or
prove a sufficient transfer budget. Frozen inputs are unchanged.
No mathematical numerical evaluation is used.

## 1. Original source and statement

Use the exact notation of the
[trailing determinant theorem](research_mixed_next_outgoing_trailing_determinants.md):
\[
\begin{gathered}
 D=N-1,\quad M=\lceil N/2\rceil,\quad
 \epsilon=N^{-1},\quad \theta=\pi/N,\quad q=e^{i\theta},\quad r=q^{-2},\\
 s_j=2\sin(j\theta),\qquad S_b=\prod_{j=1}^b s_j,\qquad S_D=N,\\
 C_{b,N}(Z)=\sum_{k=0}^{D}
 \frac{(r^b)^{-k}(r^{b+1};r)_k(rZ;r)_k}{(r;r)_k^2}.
\end{gathered}                                                     \tag{1}
\]
The literal stop in (1) is \(D-b\); the zero factors are retained.
In particular \(C_{D,N}=1\) exactly, at both parities.
Let
\[
 \mathfrak Z=\{\rho e^{-i\alpha}:
 4/5\le\rho\le8/7,\quad3\pi/5\le\alpha\le39\pi/50\}.
                                                                    \tag{2}
\]
The actual complete \(343\) references of length at least five lie
in this region.

For \(1/2\le a\le1\), put
\[
\begin{gathered}
 t=t(a)=(\pi a-\pi/2)/2,\qquad
 \sigma(a)=2\sin(\pi a),\qquad k(a)=\sigma(a)^3,\\
 V(a,Z)=3e^{it}+2e^{-3it}+Ze^{5it}.
\end{gathered}                                                     \tag{3}
\]
Let \(m(a,Z)\) be the first diagonal of the frozen half-line inverse
in the [absolute-anchor theorem](research_mixed_next_outgoing_absolute_anchor.md),
equations (4)--(5). Equivalently, it is the branch
\[
 k m^2-Vm+1=0,\qquad |\sigma^{3/2}m|<1\quad(a<1),\qquad
 m(1,Z)=\frac{e^{-i\pi/4}}{1-Z}.                                  \tag{4}
\]
Define, with primes denoting differentiation in \(a\) at fixed \(Z\),
\[
\begin{split}
 V_1(a,Z)&=\frac{i\pi}{4}
             \{3e^{it}-6e^{-3it}+Ze^{5it}\},\\
 m_1(a,Z)&=
 \frac{m(a,Z)^2\{(k(a)m(a,Z))'-V_1(a,Z)\}}
      {1-k(a)m(a,Z)^2},\\
 h(a,Z)&=e^{\,i(\pi/4-\pi a/2)}m(a,Z),\qquad
 \eta(a,Z)=\frac{i\pi}{4}+\frac{m_1(a,Z)}{m(a,Z)}.
\end{split}                                                       \tag{5}
\]
Section 2 proves that these functions are regular through \(a=1\)
and on a fixed interval slightly to the left of \(1/2\).
They are holomorphic in \(Z\) on a fixed neighborhood of (2).

Choose a continuous logarithm of \(h\), holomorphic in \(Z\), on
this parameter set, and set
\[
 \mathcal B(a,Z)=
 \exp\left\{\frac{\log h(a,Z)+\log h(1,Z)}2
                    -\int_a^1\eta(x,Z)\,dx\right\}.               \tag{6}
\]
This is nonzero. For the actual action formula below the logarithm
is fixed by the original factorial phase as specified in Section 5.

**Theorem.** Uniformly for \(Z\in\mathfrak Z\), both parities, and
\(M-1\le b\le D\), with \(a=b/N\),
\[
 \boxed{\quad
 C_{b,N}(Z)=\frac{S_b}{N}
   \exp\left\{-N\int_a^1\log h(x,Z)\,dx\right\}
   \mathcal B(a,Z)\{1+O(N^{-1})\}.
 \quad}                                                         \tag{7}
\]
The error is relative and uniform, including the literal last row.
The finite sine product is left exact in (7). No sine-product
asymptotic near its vanishing endpoint is required.

For the actual outgoing parameters
\[
 z_*=u+iv,\qquad 3/10\le u\le39/100,\qquad
 -3/100\le v\le1/50,\qquad Z=e^{-2\pi i z_*},                     \tag{8}
\]
let \(\mathcal S(a,z_*)\) be the original selected action.
On the middle interval, including the one grid step below \(1/2\)
by its original local continuation,
\[
 \boxed{\quad
 C_{b,N}(Z)=N^{-1/2}\sqrt{2\sin(\pi a)}\,
       \mathcal B(a,Z)e^{N\mathcal S(a,z_*)}
                      \{1+O(N^{-1})\},
 \qquad M-1\le b\le\lfloor5N/6\rfloor .
 \quad}                                                         \tag{9}
\]
The square root in (9) is positive for real \(a\).
At the exact half-input boundary this gives
\[
 C_{M-1,N}(Z)=N^{-1/2}\mathcal A_{\mathrm{par}}(Z)
       e^{N\mathcal S(1/2,z_*)}\{1+O(N^{-1})\},                   \tag{10}
\]
where
\[
 \mathcal A_{\mathrm{par}}(Z)=
 \sqrt2\,\mathcal B(1/2,Z)
       \exp\{-\delta_N\partial_a\mathcal S(1/2,z_*)\},\qquad
 \delta_N=
 \begin{cases}1,&N\ \mathrm{even},\\[2pt]1/2,&N\ \mathrm{odd}.
 \end{cases}                                                    \tag{11}
\]
Both amplitudes are nonzero. Formula (11) retains the original
physical grid shift rather than replacing it by the same constant
at the two parities.

The relative errors in (7), (9), and (10) are holomorphic on a fixed
\(Z\)-neighborhood of their compact parameter sets. After a fixed
shrink, each fixed number of their \(Z\)-derivatives is also
\(O(N^{-1})\). These are derivatives of the normalized relative
error; no bound for an unnormalized derivative is implicit.

## 2. Uniform regularity of the stable branch

The full-tail energy estimate, in the notation of the
[absolute-anchor theorem, equation (13)](research_mixed_next_outgoing_absolute_anchor.md),
gives a fixed continuous real rotation \(\beta(a)\) for which
\[
 \Re V-\beta(a)\Im V-2\sigma^{3/2}>51/350
                         \qquad(1/2\le a\le1,\ Z\in\mathfrak Z).
                                                                    \tag{12}
\]
The frozen half-line inverse is uniformly bounded. Its first
diagonal is nonzero, and (4) selects its stable root. By compactness,
including the scalar endpoint at \(a=1\), there are fixed constants
\[
 0<c_m\le |m|\le C_m,\qquad |k m^2|\le\rho_0<1.                 \tag{13}
\]
The strict upper bound follows from (4) for \(a<1\) and from
\(k(1)=0\) at the endpoint.

Although the off-diagonal coefficient \(\sigma^{3/2}\) need not
be analytically continued at \(a=1\), the algebraic equation in
(4) uses only the analytic coefficient \(k=\sigma^3\). Its
derivative in \(m\) is
\[
 2km-V=\frac{km^2-1}{m}\ne0.                                  \tag{14}
\]
The implicit-function theorem therefore continues \(m\)
holomorphically in \(a\) and \(Z\) to a fixed neighborhood of
the closed interval and compact region. The local continuations
agree on overlaps with the already selected stable branch.
Shrinking the neighborhoods, (13) persists with a slightly larger
constant less than one. All fixed derivatives required below are
uniformly bounded.

One may take a simply connected open sector neighborhood of
\(\mathfrak Z\) and a thin interval neighborhood in \(a\).
The continued \(h\) is nonzero there, so a continuous logarithm
exists, holomorphic in \(Z\) and real analytic in \(a\).
In particular (5)--(6) have no terminal singularity.
At \(a=1\),
\[
                  h(1,Z)=-\frac{i}{1-Z}.                       \tag{15}
\]
The implicit continuation also defines the functions in (5)--(6)
at \(b/N<1/2\) when \(b=M-1\), for all sufficiently large levels.
No finite recurrence outside its original physical range is used.

The energy and trailing determinant proofs persist on a fixed
complex \(Z\)-neighborhood: changing \(Z\) is a uniformly small
diagonal perturbation of every normalized finite or half-line
operator. Thus all trailing inverses remain holomorphic and
uniformly bounded on a common neighborhood, independently of
the number of rows. This will permit the normalized Cauchy
estimates in Section 6.

## 3. The exact finite Riccati equation and its first correction

Let
\[
 \mathfrak m_{b,N}
   =(H_{b,N}^{-1})_{0,0},\qquad M\le b\le D,                    \tag{16}
\]
where \(H_{b,N}\) is the exact normalized trailing matrix in
the [absolute-anchor theorem, equations (18)--(20)](research_mixed_next_outgoing_absolute_anchor.md).
Its diagonal at the original row \(b\) is
\[
 V_N(a,Z)=3e^{i(t+\pi\epsilon/4)}
       +2\cos(\pi\epsilon)e^{-i(3t+3\pi\epsilon/4)}
       +Ze^{i(5t+\pi\epsilon/4)}.
                                                                    \tag{17}
\]
The product of its upper and lower entries between rows \(b\)
and \(b+1\) is exactly \(s_{b+1}^3=k(a+\epsilon)\).
Every trailing block is invertible, by the original energy
theorem with the natural terminal row retained. Its Schur
complement consequently gives
\[
 \mathfrak m_{b,N}
  =\frac1{V_N(a,Z)-k(a+\epsilon)\mathfrak m_{b+1,N}}
                \quad(M\le b<D),\qquad
 \mathfrak m_{D,N}=\frac1{V_N(D/N,Z)}.                           \tag{18}
\]
At \(b=D\), the omitted term has the exact coefficient
\(k(1)=0\). There is no metric factor \(S_N\), nor a fictitious
nonzero last coupling.

Taylor expansion of the explicit trigonometric polynomial (17)
gives, uniformly on the fixed parameter neighborhood,
\[
                  V_N=V+\epsilon V_1+O(\epsilon^2).             \tag{19}
\]
Define \(\widetilde m_N(a)=m(a)+\epsilon m_1(a)\).
The first-order expansion of the right side of (18), evaluated
at \(\widetilde m_N(a+\epsilon)\), is
\[
 m+\epsilon m^2\{(km)'+km_1-V_1\}+O(\epsilon^2).
\]
Equality of its first-order term with \(\epsilon m_1\) is
precisely (5). Thus
\[
 \widetilde m_N(a)-
 \frac1{V_N(a,Z)-k(a+\epsilon)\widetilde m_N(a+\epsilon)}
                         =O(\epsilon^2).                       \tag{20}
\]
This estimate holds uniformly through \(a=1-\epsilon\).
At that endpoint it says
\(\widetilde m_N(D/N)-V_N(D/N)^{-1}=O(\epsilon^2)\),
because the coefficient of the next value is zero.

For completeness, the residual in (20) propagates with a fixed
contraction, not merely with a bound on distinct characteristic
roots. Put
\[
 F_{a,N}(w)=\{V_N(a,Z)-k(a+\epsilon)w\}^{-1}.
\]
At \(w=m(a+\epsilon)\), its derivative converges uniformly to
\(k(a)m(a)^2\). Equation (13), continuity, and the nonzero
denominators give a fixed radius \(r_*>0\), a number
\(\rho_1<1\), and all sufficiently large \(N\), such that
\[
 |F_{a,N}(w)-F_{a,N}(w')|
       \le\rho_1|w-w'|                                        \tag{21}
\]
whenever \(w,w'\) are in the \(r_*\)-disc about
\(\widetilde m_N(a+\epsilon)\), throughout the required
real grid and the smaller fixed \(Z\)-neighborhood.

Starting with the exact last equation in (18), backward induction
now proves
\[
 \boxed{\quad
 \mathfrak m_{b,N}=m(b/N,Z)+N^{-1}m_1(b/N,Z)+O(N^{-2}),
                      \qquad M\le b\le D .
 \quad}                                                        \tag{22}
\]
Indeed a residual bound \(C\epsilon^2\), together with (21),
propagates an error at most
\(C\epsilon^2/(1-\rho_1)\); for large \(N\) this remains inside
the fixed disc at every step. The initial error at \(D\) is
already bounded by (20). This proves (22) without assuming a
finite packet and without losing accuracy near the terminating
sine zero.

## 4. Exact ratio multiplication and the leading amplitude

The trailing determinant identity fixes both the sign and the
normalization:
\[
 \frac{C_{b,N}}{C_{b-1,N}}
   =-A(b/N)w_b\,\mathfrak m_{b,N},\qquad
 A(a)=e^{-2\pi ia}(e^{-2\pi ia}-1),\quad
 w_b=e^{i\pi/(4N)}\{-e^{5it(b/N)}\}.
                                                                    \tag{23}
\]
Direct multiplication, with \(\sigma(a)>0\) for \(a<1\), gives
\[
 -A(a)\{-e^{5it(a)}\}
        =\sigma(a)e^{\,i(\pi/4-\pi a/2)}.
\]
Since \(m\) is uniformly separated from zero, (22) yields the
relative ratio expansion
\[
 \frac{C_{b,N}}{C_{b-1,N}}
 =s_b h(b/N,Z)
       \{1+N^{-1}\eta(b/N,Z)+O(N^{-2})\},
                         \qquad M\le b\le D.                   \tag{24}
\]
The small factor \(s_b\) is exact on both sides; it is never
divided into an absolute error.

Invert the product of (24) from \(j=b+1\) to \(D\) and use the
literal value \(C_{D,N}=1\). The product of the \(s_j\)'s is
\(N/S_b\). The logarithm of the bracket in (24) is its small,
near-zero logarithm. It gives, uniformly for \(M-1\le b\le D\),
\[
 C_{b,N}=\frac{S_b}{N}
 \exp\left\{-\sum_{j=b+1}^{N-1}\log h(j/N,Z)
       -\frac1N\sum_{j=b+1}^{N-1}\eta(j/N,Z)+O(N^{-1})\right\}.
                                                                    \tag{25}
\]
The empty sums at \(D\) are included. This is an identity of
complex products with a controlled relative error; no modulus
has been taken.

Uniform Euler--Maclaurin comparison for the smooth functions in
(25) gives, for \(a=b/N\),
\[
\begin{split}
 \sum_{j=b+1}^{N-1}\log h(j/N,Z)
    &=N\int_a^1\log h(x,Z)\,dx
                  -\frac{\log h(a,Z)+\log h(1,Z)}2+O(N^{-1}),\\
 \frac1N\sum_{j=b+1}^{N-1}\eta(j/N,Z)
    &=\int_a^1\eta(x,Z)\,dx+O(N^{-1}).
\end{split}                                                       \tag{26}
\]
The bounds hold also when there are no interior grid points:
Taylor expansion at \(1\) then gives the same endpoint formula.
Equations (25)--(26) prove (7).

Changing the chosen \(\log h\) by \(2\pi i\ell\),
\(\ell\in\mathbb Z\), leaves \(\mathcal B\) unchanged. Its effect
on the integral factor in (7) is
\(e^{-2\pi i\ell N(1-a)}=e^{-2\pi i\ell(N-b)}=1\).
Thus the finite-grid formula is independent of that logarithmic
choice. The original phase fixes a particular choice for (9).

## 5. Original factorial action, without a hidden imaginary constant

The [terminal-normalization theorem](research_mixed_next_outgoing_action_terminal_normalization.md)
constructs the original zero-lift critical value
\(\widetilde{\mathcal S}(a,z_*)\) on \(1/2\le a<1\).
It uses the original primitive, proves
\[
 \lim_{a\uparrow1}\widetilde{\mathcal S}(a,z_*)=0,
 \qquad
 e^{\partial_a\widetilde{\mathcal S}(a,z_*)}
       =-A(a)\{-e^{5it(a)}\}m(a,Z)=\sigma(a)h(a,Z),             \tag{27}
\]
and agrees with \(\mathcal S\) on the original middle interval.

Choose the branch of \(\log h\) at \(a=1/2\) so that
\[
 \log h(1/2,Z)
   =\partial_a\mathcal S(1/2,z_*)-\log2.                        \tag{28}
\]
The parameter rectangle is connected. The right side is a
logarithm of \(h\), so (28) agrees with a single holomorphic
logarithm on a neighborhood; any initial discrepancy from the
logarithm of Section 2 is one constant integer multiple of
\(2\pi i\). Extend that choice along \(a\).
By (27) and continuity,
\[
 \partial_a\widetilde{\mathcal S}
          =\log\sigma+\log h
                             \qquad(1/2\le a<1).               \tag{29}
\]
The difference belongs to \(2\pi i\mathbb Z\) and is zero at
\(1/2\), so it cannot change. The chosen logarithm of \(h\)
extends finitely to \(a=1\) by Section 2. Hence (29) has only
the integrable real singularity \(\log\sigma\).

Write
\[
 J(a)=\int_0^a\log(2\sin\pi x)\,dx,\qquad J(1)=0.
\]
Integrating (29), using the original terminal value in (27),
proves the **complex**, not merely real, identity
\[
 \widetilde{\mathcal S}(a,z_*)
       =J(a)-\int_a^1\log h(x,Z)\,dx.                           \tag{30}
\]
This retains the original additive constant and logarithmic lift.
It uses only the continued critical value; it does not assert
that a finite contour follows that critical point beyond its
proved contour domain.

At \(a=1/2\), the selected critical point is simple and all its
original shifted arguments have uniform strict strip guards on
the compact set (8). Its original phase and critical value
therefore extend holomorphically to a fixed neighborhood of
that face. The same is true of the right side of (30).
Their agreement extends (30) slightly to the left of \(1/2\).
This justifies its use at \(a=(M-1)/N\).

On every compact subinterval of \((0,1)\), the finite sine
product has the uniform expansion
\[
 \frac{S_b}{N}
  =N^{-1/2}\sqrt{2\sin(\pi a)}
       e^{NJ(a)}\{1+O(N^{-1})\},\qquad a=b/N.                  \tag{31}
\]
One direct normalization check writes
\(\log(2\sin\pi x)=\log(2\pi x)+f(x)\), where
\(f(x)=\log(\sin\pi x/(\pi x))\) is smooth at zero.
Stirling's formula for \(b!\) and Euler--Maclaurin for
\(\sum_{j=1}^b f(j/N)\) give the prefactor
\[
 \sqrt{2\pi aN}\,\exp(f(a)/2)=\sqrt{2N\sin(\pi a)}
\]
before division by \(N\). Their uniform errors are \(O(N^{-1})\).
This proves (31) with the displayed constant.

Substituting (30)--(31) into (7) proves (9).
Finally
\[
 \frac{M-1}{N}=\frac12-\frac{\delta_N}{N}
\]
with the two values of \(\delta_N\) in (11).
Taylor expansion of the original analytic action and of the
nonzero amplitude at \(1/2\) proves (10)--(11).
As a consistency check with the exact products, the two
amplitudes can equivalently be written
\[
 \mathcal A_{\rm even}
       =\frac{\mathcal B(1/2,Z)}{\sqrt2\,h(1/2,Z)},\qquad
 \mathcal A_{\rm odd}
       =\mathcal B(1/2,Z)
                  \exp\{-\tfrac12\log h(1/2,Z)\}.              \tag{32}
\]
The logarithm in the odd expression is the original choice (28).

## 6. Holomorphic relative errors and remaining scope

Every step in (18)--(26) holds on one fixed complex
\(Z\)-neighborhood of the closed set (2), after shrinking it
once. The exact finite source and all its trailing inverses
are holomorphic there. The leading terms in (7) are holomorphic
and nonzero. Consequently the normalized error
\[
 \mathcal R_{b,N}(Z)=
 \frac{C_{b,N}(Z)}
 {(S_b/N)\exp\{-N\int_{b/N}^1\log h\}\mathcal B(b/N,Z)}-1
\]
is holomorphic and uniformly \(O(N^{-1})\).
Cauchy's formula on fixed smaller neighborhoods gives the same
order for every fixed \(Z\)-derivative. The same argument applies
to the normalized formulas (9)--(10), using the original local
action branch. Composing with \(Z=e^{-2\pi iz_*}\) gives fixed
normalized outgoing-coordinate derivatives as well.

The result fixes the complex amplitude of the actual complete
polynomial, all its original finite stops, and both parity
constants. It does not remove or estimate the exact retained
small-\(k\) subtraction when a different source is requested.
In particular the original remaining observation still has
its literal inner-period factors and phases:
\[
 \frac1{\kappa_N^2N}
       \sum_{b=M}^{D}(-q)^b\lambda_b C_{b,N}(Z_*),
 \qquad \lambda_b=\phi_N(R^3e_bQ_N^{\rm full}).                  \tag{33}
\]
An \(O(N^{-1})\) relative error may not be discarded inside that
further coherent sum. No bound for (33), sufficient attachment
gap, or finite-exception theorem follows from the present
amplitude calculation alone.

## Frozen source bindings

- Complete trailing determinants and natural last row:
  8564c705a0c8cd96cb7211c10166a522dde511bda27a94ac18a7cdafccf0b47f.
- Actual finite outgoing ratio transport:
  2bf8a2f401b3472da0d250c97403fa776396e3dd524bd149a9209b6f8eacdeaf.
- Full-tail weighted energy:
  0037a31d5f2a8cedea53d70bf1f0434f906668fe0934e5ee303890a8b3eceee7.
- Absolute terminating anchor:
  51c9e5f1a47be3d9f3e1fa756e390a98c07f84c33f1aa0ad5ee5b948771229ab.
- Original terminal action normalization:
  5b46b329c54cf252fc9d52f91e546fda47eadcfb2a0b62b842881c1bd2d87ce4.
- Original selected outgoing sheet:
  850d97273259d39b0fc0ecf89bedaddceb97b13555c38a95d1f3e9fa7643067d.

The proof uses exact recurrence identities and uniform written
analytic estimates only. No numerical evaluation, saved-value
calculation, or replay was performed.

