# The complete three/four prefix after the boundary transform

Research assembly, 7 November 2026. The original three/four pair has
a nonzero asymptotic after the exact inverse boundary transform, near
its original right private geometric coordinate. This statement concerns
the entire transformed finite polynomial. Its proof estimates every
part of one deformed incoming contour, including all physical rows
that cease to vanish when the outgoing coordinate becomes complex.

The outgoing neighborhood is local to this particular reference. A
uniform theorem at the references selected by arbitrary following
short tangles is a further assertion.

## 1. The finite polynomial and its action

Keep the original conventions
\[
 r=e^{-2\pi i/N},\qquad P_j=(r;r)_j,\qquad p_j(X)=(rX;r)_j,
\]
and the complete functions
\[
 \begin{split}
 U_{0,N}(w,X)&=\sum_{j=0}^{N-1}
                    H_N(w,r^{-j})p_j(X)/P_j,\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}
                    X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 f_{34,N}(w,Y)&=N\operatorname{CT}_X
                    [U_{0,N}(w,X)C_{1,N}(X,Y)].
 \end{split}                                                   \tag{1}
\]
Here \(\operatorname{CT}_X\) means the constant Laurent coefficient.
Both \(w\) and \(Y\) have degree less than \(N\) in the last
polynomial. The exact normalization and inverse boundary transform
are proved in [the transformed-complement note](research_mixed_three_four_transformed_complement.md),
Lemma 1. In particular (1) has no final Gram contraction, outgoing
Fourier halfweight, or factor \(\kappa_N\).

Let \(a_*=A+ic\), \(t_*=T+ih_t\), and \(z_*\) be the
original shared coordinate, terminal transform coordinate, and right
private coordinate of the complete ordinary pair. Its calibrated
prefix action is
\[
 \begin{split}
 Q(t;a,z)&=g(a+t)+g(z+t)-3g(t)-g(a)-g(z)+2\pi iat,\\
 \mathcal P_{34}(w,z)&=
    \operatorname{stat}_{a,t}[\mathcal T_0(a,w)+Q(t;a,z)].
 \end{split}                                                   \tag{2}
\]
The critical branch passes through \((a_*,t_*)\) when
\((w,z)=(-2,z_*)\). The constant and logarithmic lifts in (2)
are inherited from the original finite source. The saved-enclosure
consequences used throughout are
\[
 -7/200<c<0,\qquad |e^{-2\pi iz_*}|<5/6,
 \qquad \Re\mathcal P_{34}(-2,z_*)>181/100.              \tag{3}
\]
They are established, without reevaluation here, in
[the transformed-complement calibration](research_mixed_three_four_transformed_complement_calibration.md).
If \(E_{\rm end}\) is the removed right endpoint action, then the
original complete ordinary action is exactly
\(\mathcal P_{34}(-2,z_*)+E_{\rm end}(z_*)\).

## 2. A single exact contour and all its parts

For fixed \(N,w,Y\), the function
\[
 a\longmapsto U_{0,N}(w,e^{-2\pi ia})
                    C_{1,N}(e^{-2\pi ia},Y)
\]
is entire and one-periodic: it is a finite Laurent polynomial in
\(e^{-2\pi ia}\). Therefore (1) equals \(N\) times its integral
over any path from zero to one. Use the following successive parts:

1. the real segment \([0,1/10]\);
2. the segment \(a(x)=x+ic(x-1/10)/(3/25)\),
   \(1/10\le x\le11/50\);
3. the horizontal plateau \([11/50+ic,9/20+ic]\);
4. the horizontal right interval \([9/20+ic,1/2+ic]\);
5. the upward segment from \(1/2+ic\) to \(1/2\), followed
   by the real segment \([1/2,1]\).

The paths meet at their endpoints. Their increasing incoming
orientation agrees with extraction of the constant coefficient.
The sum of their five contributions, each with the factor \(N\),
is exactly \(f_{34,N}\); there is no quadrature or sampled-sum
approximation in this decomposition.

The needed source estimates are as follows. A positive gap means
exponential decay after multiplication by
\(e^{-N\mathcal P_{34}(w,z)}\), on a fixed neighborhood of
\((-2,z_*)\).

| Incoming part | Complete-source result |
|---|---|
| Real initial interval | [Initial-interval theorem](research_mixed_transformed_real_initial_interval.md): its entire integral has gap \(1/20\) |
| Left transition interval | [Transformed left-taper theorem](research_mixed_three_four_transformed_left_taper.md): the whole conditional sum and its integral have a positive gap |
| Central plateau | [Transformed plateau theorem](research_mixed_three_four_transformed_plateau_source.md): a nonzero holomorphic stationary-phase asymptotic for its exact integral |
| Right interval | [Transformed right-strip theorem](research_mixed_transformed_right_strip.md): the whole conditional sum has gap \(1/500000\) before its bounded-length integration |
| Vertical connector and real far half | [Transformed-complement calibration](research_mixed_three_four_transformed_complement_calibration.md): the entire integral has gap \(1/1000\) |

The restored upper rows on the plateau and right interval are covered
by [the upper-row theorem](research_mixed_transformed_upper_rows.md).
On the left transition interval they use the separate angle and radius
comparison in [the left upper-row theorem](research_mixed_transformed_left_upper_rows.md).
Neither argument assumes the physical triangular support persists
after the outgoing variable has moved off its grid.

Every source estimate is for the original finite polynomial or for
an exact contour contribution from it. The terminal comparisons used
in these proofs are pointwise before the private coordinate is
summed. Removing their known nonzero endpoint factor consequently
produces the conditional interpolant in (1). No estimate for the
already summed terminal function is divided by that factor.

## 3. The nonzero asymptotic for the whole polynomial

**Theorem 1.** There are a fixed complex neighborhood \(\mathcal U\)
of \((-2,z_*)\) and a zero-free holomorphic function
\(\mathcal A_{34}\) on it such that
\[
 f_{34,N}(w,e^{-2\pi iz})
   =N^{-3/2}\mathcal A_{34}(w,z)
       e^{N\mathcal P_{34}(w,z)}
                         (1+\varepsilon_N(w,z)),
 \qquad \varepsilon_N=O_{\rm hol}(N^{-1}).              \tag{4}
\]
The assertion holds at all sufficiently large integer levels, with
both parities. Every fixed mixed derivative of \(\varepsilon_N\)
is \(O(N^{-1})\) on smaller neighborhoods.

*Proof.* Intersect the five fixed parameter neighborhoods in the
table and shrink once to a relatively compact neighborhood of the
reference. The plateau theorem gives (4) for its own exact integral,
with \(\mathcal A_{34}=\mathcal A_P\) from that theorem. Its
explicit coefficient is
\[
 \mathcal A_{34}(w,z)=
 \frac{2\pi\,\mathcal B_0(a^\#,w)b(a^\#,t^\#,z)}
 {\sqrt{\det[-\partial_{(a,t)}^2
       (\mathcal T_0(a,w)+Q(t;a,z))]_{(a^\#,t^\#)}}}.     \tag{5}
\]
Here \((a^\#,t^\#)\) is the critical branch in (2),
\(\mathcal B_0\) is the leading coefficient of the complete
first cap, and \(b\) is the conditional row coefficient defined
in the plateau theorem. Each is nonzero. The determinant uses the
original accretive Gaussian branch.

For the other four parts, the table supplies a fixed positive gap
in the same normalization. Their path lengths and Jacobians are
bounded. An extra factor \(N\) where necessary, and all polynomial
prefactors, can be paid by reducing those gaps. Their sum is therefore
\(O(e^{-\gamma N})\) after normalization, for some fixed
\(\gamma>0\). Since \(\mathcal A_{34}\) is bounded away from
zero on the smaller neighborhood, this is an exponentially small
relative error compared with the plateau's \(N^{-3/2}\) prefactor.
Adding the exact five contributions proves (4). Holomorphy and Cauchy
estimates on nested neighborhoods prove the derivative assertion.
\(\square\)

In particular the full transformed polynomial has an actual lower
bound on every compact subset of \(\mathcal U\): for sufficiently
large \(N\),
\[
 \frac12 N^{-3/2}|\mathcal A_{34}(w,z)|
       e^{N\Re\mathcal P_{34}(w,z)}
 \le |f_{34,N}(w,e^{-2\pi iz})|
 \le\frac32 N^{-3/2}|\mathcal A_{34}(w,z)|
       e^{N\Re\mathcal P_{34}(w,z)}.                  \tag{6}
\]
Thus its logarithmic growth there is \(\Re\mathcal P_{34}\).
This conclusion is obtained from a nonzero coefficient and a bound
for every other contribution, not from an upper norm estimate alone.

## 4. What this supplies for further composition

Equation (4) concerns the exact polynomial in the boundary coordinates
needed for further contraction. It therefore resolves the previously
missing complete-prefix asymptotic at the original pair's private
reference. It is stronger than knowing the original ordinary closure
at one color, since taking its inverse boundary transform with an
uncontrolled matrix norm would not preserve an exponential gap.

The next attachment still requires the estimates at the reference
selected by that attachment, together with bounds outside its local
critical neighborhood. Since the current prefix ends in type four,
the complete factor \(d_N(Y)(1+Y^{-N})\) occurs for either next
letter, three or four. The exact conditional transfer incorporates
the intervening Gram contraction; neither operation can be omitted.
This note does not prove that its present local
neighborhood contains all such references, that the excluded
contributions stay smaller there, or that arbitrary branching short
components can be treated this way. The all-but-finitely-many theorem
therefore remains open.
