# A weighted observation space and an exact local-composition obstruction

Private source deduction, 9 November 2026. The new complete outer-mode
upper bound defines a useful norm on the actual radical test space.
Fixed-degree ordinary Casimir insertions preserve that norm up to a
polynomial factor. In particular they preserve the proved exponential
suppression of the right attachment. This is not a bound for a whole
fixed crossing or turn.

There is also an exact obstruction to propagating only the new local
transfer packet: one original unweighted conditional transfer can
amplify an error exponentially small on the local outgoing disk.
The example is a polynomial message, not an asserted knot prefix.
No numerical evaluation, import, compilation or frozen-source edit
is used.

## 1. The original radical test space

Retain
\[
 D=N-1,\qquad m=\lfloor N/2\rfloor,\qquad M=\lceil N/2\rceil,
 \qquad U=m-1,\qquad q=e^{\pi i/N}.
 \tag{1}
\]
The original spectral relation and its double-node polynomial are
\[
 \begin{split}
 P_N(X)&=2T_N(X/2)+2,\\
 Q_{d,N}(X)&=
 \begin{cases}
 2T_m(X/2),&N=2m,\\
 U_m(X/2)-U_{m-1}(X/2),&N=2m+1.
 \end{cases}
 \end{split}
 \tag{2}
\]
Here the symbols \(T_j,U_j\) in (2) are the usual Chebyshev
polynomials. The exact factorizations are
\[
 P_N=
 \begin{cases}
 Q_{d,N}^{\,2},&N=2m,\\
 (X+2)Q_{d,N}^{\,2},&N=2m+1.
 \end{cases}
 \tag{3}
\]
They follow either from the double-angle identities or the original
physical-node factorization. The ordinary Newton polynomial \(e_M\)
is a nonzero scalar multiple of \(Q_{d,N}\) at even levels and of
\((X+2)Q_{d,N}\) at odd levels. Consequently
\[
                         e_M Q_{d,N}=0
                  \quad\hbox{in }\mathbb C[X]/(P_N).
 \tag{4}
\]
This is an identity in the full Hermite quotient. At a double node
both its value and first normal vanish; at the odd simple node its
factor \(X+2\) vanishes. No trace has been replaced by a distinct-node
trace.

For every incoming ordinary color \(w\), keep the exact functional
\[
 \mathcal L_{N,w}(h)
  =\phi_N\!\left[R_N^3 e_M Q_{N,w}^{\rm full}h\right],
 \qquad
 Q_{N,w}^{\rm full}(X)
  =\phi_N^{(x)}[R_N(x)^3K_N(w,x)K_N(x,X)].
 \tag{5}
\]
Equation (4) shows that its test argument belongs naturally to
\[
 \mathcal E_N=\mathbb C[X]/(Q_{d,N}),\qquad
 h=\sum_{k=0}^{U}h_k B_k(X),\qquad B_k(X)=T_k(-X/2).
 \tag{6}
\]
The representative in (6) is unique. All coefficients may be
complex. Reduction in (6) is used only after the factor \(e_M\);
it is not a reduction of an arbitrary free boundary polynomial.

Let the original selected charged action be \(\Gamma(\delta)\),
with its original complete normalization \(M_3=\Gamma(0)\).
The adopted phase results give
\[
 \Gamma'(\delta)=-K_\delta,\qquad
 0\le K_\delta\le2/5,\qquad 0\le\delta\le1/2.
 \tag{7}
\]
Define a level-dependent weighted coefficient norm by
\[
 \omega_{k,N}=\exp\!\left[N\Gamma(1/2-k/N)\right],
 \qquad
 \|h\|_{\Gamma,N}=\sum_{k=0}^{U}|h_k|\omega_{k,N}.
 \tag{8}
\]
These weights are nondecreasing in \(k\), and
\[
              1\le\frac{\omega_{k+1,N}}{\omega_{k,N}}
                         \le e^{2/5}.
 \tag{9}
\]
Indeed the logarithm of this ratio is the integral of \(NK_\delta\)
over an interval of length \(1/N\). This uses the proved action
derivative, not a numerical estimate of the weights.

**Proposition 1.** For every fixed \(\varepsilon>0\),
\[
 \sup_{w\in[-2,2]}|\mathcal L_{N,w}(h)|
       \le C_\varepsilon e^{N\varepsilon}\|h\|_{\Gamma,N}
       \qquad(h\in\mathcal E_N)
 \tag{10}
\]
at both parities and all sufficiently large levels.

*Proof.* The complete incoming-color outer theorem proves
\[
 |\mathcal L_{N,w}(B_k)|
       \le C_\varepsilon e^{N\varepsilon}\omega_{k,N}
                    \quad(0\le k\le U,\ w\in[-2,2]).
 \tag{11}
\]
Expand the exact test representative (6). The triangle inequality
is applied to these already coherent complete observations, not to
their inner finite sums. This proves (10).

More precisely, the dual norm of this exact functional is
\[
 \|\mathcal L_{N,w}\|_{\Gamma,N}^{*}
       =\max_{0\le k\le U}
                   \frac{|\mathcal L_{N,w}(B_k)|}{\omega_{k,N}}.
 \tag{12}
\]
The upper bound follows as above, and a single nonzero basis
coefficient attains the largest ratio. Thus (10) identifies a
specific proved dual norm, rather than a bound in a freely chosen
positive nodal metric. \(\square\)

## 2. Fixed-degree Casimir insertions preserve the observation bound

Write \(\mathsf X_Nh=[Xh]\) for multiplication by \(X\) followed
by reduction in (6). We record both endpoint rules explicitly.
For all sufficiently large \(N\), so that \(m\ge3\),
\[
 \mathsf X_NB_0=-2B_1,\qquad
 \mathsf X_NB_k=-B_{k+1}-B_{k-1}\quad(1\le k\le m-2).
 \tag{13}
\]
At the last basis vector the exact folds are
\[
 B_m=0\quad(N=2m),\qquad
 B_m=-\frac12B_0-\sum_{k=1}^{m-1}B_k\quad(N=2m+1).
 \tag{14}
\]
For the even case (14) is (2). In the odd case set
\(X=-2\cos u\) and use the polynomial identity
\[
 Q_{d,N}(-2\cos u)
   =(-1)^m\frac{\sin((m+1/2)u)}{\sin(u/2)}
   =(-1)^m\left(1+2\sum_{k=1}^{m}\cos(ku)\right).
 \tag{15}
\]
The quotient is understood at its removable angular endpoints.
Thus the relation is polynomial, not merely an assertion at
noncoalescing samples.

Equations (13)--(14) give the last column by
\(\mathsf X_NB_{m-1}=-B_m-B_{m-2}\).
Using monotonicity of the weights, its odd weighted column sum is
at most
\[
 \omega_{m-2,N}+\tfrac12\omega_{0,N}
              +\sum_{k=1}^{m-1}\omega_{k,N}
       \le (m+\tfrac12)\omega_{m-1,N}.
 \tag{16}
\]
Possible cancellation in this column is not needed. All other
columns have weighted ratio at most \(2e^{2/5}\), by (9).
In particular, with the convenient common bound
\[
                         L_N=N+2e^{2/5},
 \]
we have
\[
                    \|\mathsf X_Nh\|_{\Gamma,N}
                            \le L_N\|h\|_{\Gamma,N}.
 \tag{17}
\]
The dense odd last column has been paid; it has not been replaced
by the even endpoint relation.

For an ordinary polynomial \(p_N(X)=\sum_{j=0}^{d}a_{j,N}X^j\),
functional calculus for the exact quotient gives
\[
 \|[p_Nh]\|_{\Gamma,N}
       \le \left(\sum_{j=0}^{d}|a_{j,N}|L_N^j\right)
                                                  \|h\|_{\Gamma,N}.
 \tag{18}
\]
Thus if \(d\) is fixed and the coefficients grow at most
polynomially in \(N\), its entire insertion costs only a polynomial.
Combining (4), (10), and (18) proves
\[
 \sup_{w\in[-2,2]}|\mathcal L_{N,w}(p_Nh)|
       \le C_\varepsilon N^A e^{N\varepsilon}
                                               \|h\|_{\Gamma,N}.
 \tag{19}
\]
The original full functional is on the left; quotient multiplication
has only computed its exact test class.

Here is a consequence for an actual source already estimated. Retain
the complete \(F_N^+(X,Z)\), \(P(w,z)\), \(Z_*=e^{-2\pi iz_*}\),
\(\Lambda_*=\Re P(-2,z_*)\), and
\(g_0=1/(2\cdot10^{13})\) of the incoming-color outer theorem.
For a polynomial \(p_N\) as in (18), define
\[
 \mathcal R_{N,p}^{+}(w,Z)
       =\frac1{\kappa_N^2N}
                         \mathcal L_{N,w}(p_NF_N^+(\cdot,Z)).
 \tag{20}
\]
This is an explicitly inserted version of the original right
contribution, with all its outgoing rows retained.
The complete coefficient proof in that theorem gives, on a fixed
disk about \(Z_*\), for every \(\varepsilon>0\),
\[
 \|F_N^+(\cdot,Z)\|_{\Gamma,N}
      \le C_\varepsilon N^A
                    e^{N(\Lambda_*-g_0+\varepsilon)}.
 \tag{21}
\]
The whole-frequency endpoint dominance is precisely what bounds
this coefficient sum.
Equations (19)--(21) prove
\[
 \sup_{w\in[-2,2]}|\mathcal R_{N,p}^{+}(w,Z)|
      \le C_\varepsilon N^{A'}
                    e^{N(\Lambda_*-g_0+2\varepsilon)}.
 \tag{22}
\]
Its incoming degree is still at most \(D\). Apply the same
degree-\(D\) ellipse continuation and action-continuity allocation
as Section 7 of that theorem. The extra fixed polynomial factor
in (18) is absorbed in the same prescribed allowance. We obtain
fixed disks \(B,V\) about \(-2,z_*\) on which
\[
 \left|e^{-NP(w,z)}
       \mathcal R_{N,p}^{+}(w,e^{-2\pi iz})\right|
                    \le C e^{-g_0N/2}.
 \tag{23}
\]
Every fixed mixed derivative of the normalized expression has
the same bound on smaller disks, by Cauchy's formula.
The disks may depend on the fixed insertion and coefficient
growth bound, and are chosen before \(N\).

Equation (23) is an upper estimate for the inserted right source.
It does not assert that the correspondingly inserted local
geometric coefficient is nonzero, or that an arbitrary new
whole transfer has already been assembled.

## 3. The exact profile condition for further operator composition

If an original operation actually descends to an endomorphism
\(\mathsf A_N:\mathcal E_N\to\mathcal E_N\), write its exact matrix
in (6) as \(a_{\ell k,N}\). Its induced norm is exactly
\[
 \|\mathsf A_N\|_{\Gamma,N}
       =\max_k\sum_{\ell=0}^{U}
          |a_{\ell k,N}|\frac{\omega_{\ell,N}}{\omega_{k,N}}.
 \tag{24}
\]
The upper inequality is the triangle inequality. A test supported
on one maximizing input basis vector gives equality.
The norm of a composition is bounded by the product of these norms.
Consequently bounds
\[
 \|\mathsf A_{j,N}\|_{\Gamma,N}\le C_jN^{A_j}e^{N\epsilon_j}
 \tag{25}
\]
propagate (10) with the additional rate \(\sum_j\epsilon_j\).
This is a sufficient upper-bound induction with an identified
source norm.

For example, a uniform matrix-entry profile
\[
 |a_{\ell k,N}|\le CN^A e^{N\mathcal A(\ell/N,k/N)}
 \]
gives the explicit sufficient operator rate
\[
 \sup_{s,t\in[0,1/2]}
 \left\{\mathcal A(s,t)
            +\Gamma(1/2-s)-\Gamma(1/2-t)\right\}.
 \tag{26}
\]
One may instead retain the exact finite maximum in (24).
No favorable value of (26) for a new crossing or turn is claimed.
In particular an operation which creates values outside the
radical test ideal needs its exact extra normal terms first;
it is not silently an endomorphism in (24).

For a general original fixed short crossing, the canonical
degree bound grows with \(N\); no fixed-degree bound independent
of \(N\) is supplied by (18). A turn changes the boundary
polarization. Hence neither is covered merely by the
fixed-degree assertion (18). Even an upper induction of the
form (25) would not provide a nonzero observed geometric
coefficient. The exact source-line/complement criterion in the
observation-composition note additionally requires its feedback,
complement and actual closing-row bounds. A local packet does
not estimate those blocks.

## 4. A local packet and degree alone cannot propagate an error

This obstruction uses one literal original conditional transfer.
Put \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\[
 p_j(X)=(rX;r)_j,\qquad
 C_{\beta,N}(X,Y)
    =\sum_{j=0}^{D}
          \frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\beta}},
                 \qquad \beta\in\{0,1\}.
 \tag{27}
\]
On polynomial messages of degree at most \(D\), the exact
unweighted transfer is
\[
 (\mathsf T_{0\beta,N}f)(Y)
       =N\operatorname{CT}_X[f(X)C_{\beta,N}(X,Y)]
       =\sum_{a=0}^{D}f(r^a)C_{\beta,N}(r^a,Y).
 \tag{28}
\]
There is no omitted alias here: the original \(X\)-band is
\([-D,D]\), so zero is its only multiple of \(N\).
For a weighted type-four input the separate exact formula has
the additional factor \(d_N(X)(1+X^{-N})\); (28) makes no
claim that this factor may be deleted there.

At the actual terminal physical output \(Y=r^D\),
\(p_j(Y)=0\) for every \(j\ge1\), because its first factor is
\(1-r^{D+1}=0\). Thus
\[
 C_{\beta,N}(X,r^D)=1,\qquad
                  (\mathsf T_{0\beta,N}f)(r^D)=Nf(0).
 \tag{29}
\]
Fix any nonzero \(Z_*\) and \(0<\rho<1\). The exact degree-\(D\)
message
\[
                         f_N(X)=(1-X/Z_*)^D
 \tag{30}
\]
satisfies
\[
 \sup_{|X-Z_*|\le\rho|Z_*|}|f_N(X)|\le\rho^D,\qquad
                  (\mathsf T_{0\beta,N}f_N)(r^D)=N.
 \tag{31}
\]
For every fixed derivative order \(j\), the corresponding
input derivative norm is at most
\[
                   D^j|Z_*|^{-j}\rho^{D-j};
 \tag{32}
\]
it is also exponentially small. Therefore any output norm
dominating this physical evaluation has
\[
 \|\mathsf T_{0\beta,N}\|_{\text{local disk}\to\text{output}}
                            \ge N\rho^{-D}.
 \tag{33}
\]
This is a lower bound for the exact finite operator. It
already applies when the following kernel is the original
three-type kernel, \(\beta=0\).

It also respects the normalization of a local geometric packet.
Let \(P(X)\) be any fixed holomorphic action near \(Z_*\).
Multiplying (30) by \(e^{NP(Z_*)}\), then shrinking the disk
so that
\(\sup\Re(P(Z_*)-P(X))<-\tfrac12\log\rho\), makes the
normalized input error exponentially small, with every fixed
normalized derivative on smaller disks. Its transferred value
in (29) is still exactly \(Ne^{NP(Z_*)}\).
Adding this error to a polynomial packet preserves that
packet and its fixed local jets, but the local estimates
alone do not bound the next full physical contribution.

This construction does not assert that (30) is produced by a
particular filling, nor that the actual new \(343\) remainder
has this form. It rules out only an implication whose
hypotheses are the local bidisk packet, fixed local jets and
degree bounds. Additional global source or phase-profile
information is indispensable.

The newly proved \(343\) result supplies such information for
its own right contribution through (10) and (21). To use it
inductively, the next exact source must preserve a controlled
profile such as (24), or a stricter correlated class with
verified feedback and closing estimates. Neither arbitrary
short fillings nor the per-template finite-exception theorem
follows from the local packet by itself.

## Source versions

- Full incoming-color observations and the complete right source:
  research_mixed_next_incoming_color_outer_upper_bound.md,
  5bf182877bb6905b67d68f3aafb57ec5f015b57467a9b1fb7fbff2cff2108c49.
- Original radical ideal and full physical contraction:
  research_high_newton_radical_contraction.md,
  1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03;
  research_mixed_next_inner_three_first_edge_tail_contraction.md,
  b31ac2d1cbf5f0e3ab4b71b36af9718151bced51e6959ee32b26ccf7fac5dfe6.
- Original charged action and depth:
  research_mixed_next_outer_far_nodes_and_paired_contour.md,
  4ef9ae846444c092aee5a85a36db81f8646307f3bb8d2591ccb678bed6c2bea7.
- Exact conditional source, all torus aliases and boundary conventions:
  research_mixed_conditional_torus_composition.md,
  8a25a25a95bf11767c4f305317a6fab9a9c17724ae0e24a36014b5fd8ec4f693.
- Exact literal transfer and its polynomial message space:
  research_mixed_literal_transfer_norm_obstruction.md,
  e9ce5a518439ed23b94c70eb548470ecbf9abfa5bd7c880f6828ed594a3fe0a3.
- Complement feedback and the signed closing criterion:
  research_source_adapted_observation_composition.md,
  e4a1781624d76edad35f6cc6ff3639e22b315f8314b049edaea25bc8623c0d27.
- The complete local transfer packet whose scope is being distinguished:
  research_mixed_next_transfer_complex_neighborhood.md,
  3baac5dfce1f55588166e519b5408f6d374a37ef6c3ca3b3b80731e73118f6fe.
