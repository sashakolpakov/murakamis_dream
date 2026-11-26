# Endpoint normals and a current with a larger rate than the source

Research note, 3 November 2026.

The first endpoint normal of an actual turned box is an exact
insertion in the capped source. This insertion is a simple affine
combination of the already studied odd Ward coupon. On controlled
terminal exteriors it preserves the cap's geometric exponential
rate, with an explicit \(N^2\log N\) factor.

There is also an exact example in which the complete endpoint Ward
current has a larger exponential rate than the original source to
which the contour shift is applied. The source reduces to a
hyperbolic terminal block. Thus an induction that discards endpoint
currents because their capped diagrams are simpler needs an
additional geometric comparison; complexity reduction alone does
not give a strict rate gap. The displayed example contains a
removable terminal unit crossing, so it does not refute a more
restricted criterion after all such exact reductions.

## 1. The endpoint derivative as an actual coupon

Use the original algebra \(A_N\), functional \(\phi_N\), and Newton
turn \(T\). Write
\[
 D=N-1,\quad \theta=\pi/N,\quad s_1=2\sin\theta,\quad
 c_0=2\cos\theta,\quad \eta=(-1)^D,\quad \sigma=-\eta.
 \tag{1}
\]
Let \(\Pi_0\) be the full spectral idempotent at the double root
\(c_0\), and let \(\Xi_0\) have value zero and first derivative one
there, with all other physical data zero. Put
\[
                         P_N^{\rm W}=T\Pi_0.
 \tag{2}
\]
The full local residue at \(c_0\) gives
\[
 \begin{split}
 \phi_N(A\Pi_0)&=\eta\{s_1^2 A'(c_0)-c_0 A(c_0)\},\\
 \phi_N(A\Xi_0)&=\eta s_1^2 A(c_0).
 \end{split}                                             \tag{3}
\]
The actual quarter-turn is self-adjoint for the Frobenius pairing,
and \(T\Xi_0=\eta s_1^2\,1\). Consequently, for \(F=T(A)\),
\[
 F(c_0)=\phi_N(A),\qquad F'(c_0)=\phi_N(AQ_N),             \tag{4}
\]
where
\[
 \boxed{\quad Q_N=\frac{\eta P_N^{\rm W}+c_0}{s_1^2}
       =\sum_{j=1}^{D}
           \frac{(-1)^j}{4\sin(\pi/N)\sin(\pi j/N)}e_j.
 \quad}                                                   \tag{5}
\]

To verify (5) in two ways, solve (3) for the derivative functional
and apply the self-adjoint turn. Alternatively differentiate the
literal kernel
\(F(z)=\sum_j\phi_N(Ae_j)e_j(z)\) at \(c_0\).
The factorial identity
\[
                         e_j'(c_0)=(-1)^j/(s_1s_j)
 \tag{6}
\]
gives the displayed coefficients directly. Both proofs take place
in the full quotient and retain its nilpotents.

## 2. The normal can retain the cap's full geometric rate

Let \(p\ge64\) be fixed, and set
\[
 A_{p,N}(z;u)=R^p(z)K_N(z,u),\quad
 H_{p,N}(u)=\phi_N(A_{p,N}),\quad F_{p,N}=T(A_{p,N}).
 \tag{7}
\]
The [odd Ward interpolation](research_odd_ward_logarithmic_factorial.md)
constructs an exact representative \(V_N(t)\) for \(P_N^{\rm W}\),
including its first normals. On every fixed interior saddle chart,
\[
 V_N(t)=2\sigma\log N+O(1).
 \tag{8}
\]
The same note proves, using all terms of the original terminal
contour, that
\[
 \frac{\phi_N(A_{p,N}P_N^{\rm W})}{H_{p,N}(u)}
             =V_N(t_p(u))+O_p(\log N/N).                 \tag{9}
\]
The ratios are defined on a fixed sufficiently small boundary disk
for all large levels by the nonzero terminal packet.
Equations (4)--(9) yield
\[
 \frac{F_{p,N}'(c_0;u)}{H_{p,N}(u)}
  =\frac{\eta V_N(t_p(u))+c_0+O_p(\log N/N)}{s_1^2}
  =-\frac{N^2\log N}{2\pi^2}(1+O_p(1/\log N)).
 \tag{10}
\]
In particular the value and first normal have the same exponential
rate as \(H_{p,N}\). This is a coherent asymptotic with a nonzero
coefficient, not a norm upper bound.

## 3. An exact endpoint current exceeds the original source rate

The one-step positive-power Ward difference is
\[
 W_{1,N}=2\Pi_0-\rho_N^{-1}\Xi_0,\qquad
                         \rho_N=i s_1.
 \tag{11}
\]
It is the actual cycle difference for translating the logarithmic
Gaussian window by one spectral lattice step, as proved in
[the contour-transport identity](research_gaussian_logarithmic_contour_transport.md).
This convention removes the common unit \(\kappa_N\) from the
crossing Gaussian; restoring it changes no exponential rate.

For the spectator \(F_{p,N}\), its exact current is
\[
 \begin{split}
 E_{p,N}(u)
   &=\phi_N(F_{p,N}W_{1,N})\\
   &=2\phi_N(A_{p,N}P_N^{\rm W})
                    +i\eta s_1 H_{p,N}(u).
 \end{split}                                             \tag{12}
\]
The second identity follows either from (3)--(5), or by turning
\(W_{1,N}\) before contraction:
\(T W_{1,N}=2P_N^{\rm W}+i\eta s_1\).
Thus (9) proves
\[
              \frac{E_{p,N}(u)}
                       {4\sigma\log N\,H_{p,N}(u)}
                                \longrightarrow1.       \tag{13}
\]

The original source whose Gaussian is being shifted is much simpler:
\[
 \boxed{\quad
 Z_{p,N}(u)=\phi_N(RF_{p,N})
          =\phi_N(R^{p-1}K_N(\,\cdot\,,u))
          =H_{p-1,N}(u).
 \quad}                                                   \tag{14}
\]
Indeed the original full-algebra braid identity gives \(T(R)=R^{-1}\).
Self-adjointness of \(T\) then proves (14), including all free-boundary
normals. One derivation of \(T(R)=R^{-1}\) is to use
\[
 JM^{-1}J=\kappa_N^{-1}MJM,\qquad
 M e_D=\kappa_N e_D
 \tag{15}
\]
on the unit vector; here \(M\) is original multiplication by \(R\)
and \(J\) is Newton reversal.

Choose \(p\ge65\), so the complete terminal asymptotics used above
apply to both \(p\) and \(p-1\). If \(M_{1,q}\) denotes their
complete-boundary real action, the established
[action monotonicity](research_isolated_vertex_action_gap.md)
is strict:
\[
                 \partial_q M_{1,q}=2a_q b_q/\pi>0
                    \quad(t_q=2a_q-2ib_q,\ a_q,b_q>0).
 \tag{16}
\]
At \(u=0\), equations (13)--(16) imply
\[
 \lim_{N\to\infty}\frac1N\log|E_{p,N}(0)|=M_{1,p}
       >M_{1,p-1}
       =\lim_{N\to\infty}\frac1N\log|Z_{p,N}(0)|.
 \tag{17}
\]
Both limits are along all levels. The full source on the right is
the actual hyperbolic terminal block with power \(p-1\).
The larger current therefore has to be retained and canceled in
the complete shifted identity.

## 4. Scope of the obstruction

The precise identities (4)--(5) are useful for any proposed induction:
the endpoint normal is not an unspecified new functional. Its coupon
has the exact logarithmic-factorial representative already controlled
on the physical trace strip.

What fails is the inference that a simpler capped source necessarily
has lower geometric growth than the original period. The original
source (14) contains a terminal unit crossing that can be removed
before applying contours. A strategy that first performs all such
exact reductions is not contradicted by (17). For fully reduced
short components, one still needs a geometric rate comparison for
each surviving endpoint current, or a source-preserving cancellation
of currents whose rates are too large. Neither follows from counting
the vertices removed by capping.

## 5. Reproduction

The [grouped-current script](../experiments/check_endpoint_current_matchings.py)
also checks (12) and (14) against the original crossing matrices
and monic quotient multiplication at \(N=2,\ldots,8\), for \(p=3,65\)
and a nonnodal complex boundary value. Run
~~~sh
python3 experiments/check_endpoint_current_matchings.py \
  --precision 120 \
  --output repro/results/research-endpoint-current-matchings.json
~~~
The [saved results](../repro/results/research-endpoint-current-matchings.json)
check exact finite normalizations. The strict asymptotic rate
comparison (17) follows from the written terminal and Ward theorems,
not from these finite levels.
