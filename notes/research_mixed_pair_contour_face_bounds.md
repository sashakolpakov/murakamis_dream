# Bounds for every nonprincipal contour of the mixed source

This note supplies the estimates required by the
[exact nine-term contour identity](research_mixed_pair_full_period_contour.md).
All eight nonprincipal contour families have a strict exponential
gap below the selected cubic action. The bounds retain the combined
side multiplier, the endpoint kernels, the half-grid displacements,
and the complete boundary polynomial.

## 1. Heights, phases and the inequalities

Let \(H=\Im x_*\), \(K=-\Im y_*\), for the cubic point in the
[horizontal theorem](research_mixed_two_crossing_horizontal_dominance.md).
Its exact radical enclosures give
\[
             0<H<K<79/1000,\qquad M=\Re W(x_*,y_*;0)>613/500.
                                                               \tag{1}
\]
Write \(j(a,h)=\Re J(a+ih)\), with the continued upper or lower
branch specified in that theorem. Define
\[
 \begin{split}
 \mathcal F(a,b;s,t)={}&j(a+b,s+t)-3j(a,s)-6j(b,t)+j(2b,2t)\\
                   &-\pi\{bs+(a-b-1/2)t\},
 \end{split}                                                   \tag{2}
\]
and the exact side-multiplier exponent
\[
 E(s,t)=
 \begin{cases}
  \max(0,-4\pi s-2\pi t),&s\ge0,\\
  \max(2\pi s,4\pi s-2\pi t),&s\le0.
 \end{cases}                                                   \tag{3}
\]
Both expressions agree at zero. Its role is the finite bound
\(|D_N(s,b+it)|\le8e^{NE(s,t)}\), proved from the actual rational
multiplier in the contour identity.

**Proposition 1.** Each of the following rates is strictly below
\(9/8\) on the full indicated domain:

| Family | Domain | Rate |
|---|---|---|
| Opposite horizontal contours | \(a\in[0,1],b\in[0,1/2]\), \((s,t)=(H,K),(-H,-K),(-H,K)\) | \(\mathcal F(a,b;s,t)-2\pi((-s)_++(t)_+)\) |
| Fixed \(x\), endpoint in \(y\) | \(a\in[0,1],t\in[-K,K],b=0,1/2,s=\pm H\) | \(\mathcal F(a,b;s,t)-2\pi((-s)_++(t)_+)\) |
| Combined \(x\)-sides, lower \(y\) | \(s\in[-H,H],b\in[0,1/2]\) | \(\mathcal F(0,b;s,-K)+E(s,-K)\) |
| Combined \(x\)-sides, upper \(y\) | same | \(\mathcal F(0,b;s,K)+E(s,K)-2\pi K\) |

The combined corner rates have the stronger bounds
\[
 \mathcal F(0,0;s,t)+E(s,t)-2\pi(t)_+\le3\pi K<3/4,
\]
\[
 \mathcal F(0,1/2;s,t)+E(s,t)-2\pi(t)_+\le2\pi K<3/4,
 \qquad |s|\le H,\quad |t|\le K.                        \tag{4}
\]
Here \(r_+=\max(r,0)\). All lattice penalties have their original
signs: the second variable uses the lower-base residue formula.

## 2. The corner proof

The identities \(j(0,h)=-\pi|h|/2\), \(j(1/2,h)=0\), and
\(j(1,h)=\pi|h|/2\) give
\[
 \mathcal F(0,0;s,t)/\pi
          =-|s+t|/2+3|s|/2+2|t|+t/2,                 \tag{5}
\]
\[
 \mathcal F(0,1/2;s,t)/\pi
          =3|s|/2+|t|-s/2+t.                          \tag{6}
\]
Subtract \(2(t)_+\) and add \(E/\pi\).

For (5), if \(t\ge0\), the result is \(s\) when \(s\ge0\), and
\(\min(t+s,0)\) when \(s\le0\). These are at most \(H\).
For \(t=-r\le0\), \(s\ge0\), the result is respectively
\(s+2r\) if \(s\ge r\), \(2s+r\) if \(s\le r\le2s\), and
\(3r-2s\) if \(r\ge2s\). Since \(H<K\), each is at most \(3K\).
For \(s=-q\le0,t=-r\le0\), it is \(r-q\) if \(r\le q\), and
\(3r-3q\) otherwise. This proves the first bound in (4).

For (6), the \(t\)-dependent part cancels after subtracting
\(2(t)_+\). For \(s\ge0\) the result is
\(\max(s,-3s-2t)\le2K\). For \(s=-q\le0\), it is
\(\max(0,-2q-2t)\le2K\). This proves the second bound.
Both maxima occur at \((s,t)=(0,-K)\). Finally
\(K<79/1000\) and \(\pi<22/7\) give \(3\pi K<3/4\).

## 3. Compact interval certificates

The [standalone verifier](../experiments/verify_mixed_two_crossing_contour_faces.py)
uses the exact radical heights, outward-rounded Arb/Acb balls, and
binary partitions with rational endpoints. It uses
\[
 j(a,h)=-\frac{\Im\operatorname{Li}_2(e^{-2\pi|h|+2\pi ia})}{2\pi}
                                  -\frac\pi2|h|(1-2a).
                                                               \tag{7}
\]
The two side signs in (3) are chosen by separate exact parameter
domains. No sign decision uses an interval straddling zero.

For the combined-side families it first covers
\(10^{-5}\le b\le1/2-10^{-5}\). The omitted strips are proved in
Section 4. All other compact domains are covered completely.
The [saved 128-bit certificate](../repro/results/research-mixed-two-crossing-contour-faces.json)
has the following accepted rectangle counts:

| Family | Accepted rectangles |
|---|---:|
| Lower \(y\), negative/positive \(s\) | 7,261 / 7,099 |
| Upper \(y\), negative/positive \(s\) | 432 / 810 |
| Bottom \(y\)-endpoint, negative/positive \(x\)-height | 228 / 398 |
| Top \(y\)-endpoint, negative/positive \(x\)-height | 239 / 328 |
| Horizontal \((-H,-K)\), \((H,K)\), \((-H,K)\) | 1,904 / 2,523 / 961 |

Every accepted box has its entire enclosure below \(9/8\). The
verifier checks the total covered area as an exact fraction and
records a hash of all accepted rectangles. Nonfinite enclosures
are never accepted.

There is one additional analytic safeguard near the dilogarithm
branch point. If a real-coordinate box contains an integer \(k\)
and lies within distance \(\alpha<1/4\) of it, the verifier may use
\[
          j(k,h)=\pi|h|(k-1/2),\qquad
          |j(a,h)-j(k,h)|\le m(\alpha)
                                                               \tag{8}
\]
with the proved modulus below. Thus a ball touching that branch
point is bounded by a real continuity estimate, rather than being
assigned an unverified complex branch. The integer values used are
\(k=0,1\).

This is the same standard ball-arithmetic method documented in the
references of the horizontal theorem. The exact contour identity
and the branch formulas are separate mathematical inputs.

## 4. End strips and the actual half-grid endpoints

For \(|h|\le1\), any real \(a\), and \(0<\alpha\le1/4\),
\[
 |j(a+\alpha,h)-j(a,h)|\le m(\alpha),\qquad
                  m(\alpha)=\alpha(10-\log\alpha).     \tag{9}
\]
The same bound holds for negative displacements. Indeed
\(\partial_a j=\log|2\sin\pi(a+ih)|\). Its positive part is below
8 on this height range. Its negative part is at most
\((-\log\operatorname{dist}(a,\mathbb Z))_+\), because
\(|2\sin\pi(a+ih)|\ge4\operatorname{dist}(a,\mathbb Z)\).
On an interval of length \(\alpha\le1/4\), its integral is bounded
by \(\alpha(1+\log2-\log\alpha)<\alpha(2-\log\alpha)\).
This proves (9), including intervals crossing an integer and
zero-height limits.

On all the present contours, moving \(b\) by \(0<\alpha\le1/8\) changes
(2) by at most
\[
 7m(\alpha)+m(2\alpha)+\alpha
                     \le\alpha(91-9\log\alpha).       \tag{10}
\]
The linear contribution is below \(\alpha\), since
\(\pi|s-t|<1\). Neither (3) nor the lattice penalty depends on
\(b\). Taking \(\alpha\le10^{-5}\), the right side is less than
\(199/100000\). Applying the corner bounds (4) at \(b=0,1/2\)
therefore proves the missing combined-side strips with bound
\(3/4+199/100000<9/8\). This completes Proposition 1.

The exact endpoints in the residue identity satisfy
\[
 a_N=-1/(2N),\quad b_N=1-1/(2N),\quad
 |c_N-\epsilon|,|d_N-(1/2-\epsilon)|\le1/N,
                  \qquad\epsilon=10^{-6}.             \tag{11}
\]
For \(N\ge2\cdot10^6\), the \(y\)-interval lies inside
\([\epsilon/2,1/2-\epsilon/2]\); its endpoints are within
\(2\epsilon\) of 0 and \(1/2\). Their additional rate cost from
(10) is less than \(434\cdot10^{-6}\).

Moving the real \(x\)-coordinate by \(\alpha\) costs at most
\(4m(\alpha)+\alpha\). For \(\alpha=1/(2N)\) at these levels,
this is less than \(51\cdot10^{-6}\). The estimate also applies
to the combined side, whose limiting real coordinate is zero.
It includes a factorial argument crossing an integer: no bounded
logarithmic derivative at that integer is assumed.

All actual nonprincipal contour rates are consequently below
\[
                         113/100<M.                    \tag{12}
\]
This generous common bound leaves a fixed margin for a sufficiently
small complex disk in the outside angle \(u\).

## 5. Bounds on the exact factorial factors

The phase inequalities must bound the actual integrands, including
zero-height portions. The required estimates follow from the
[uniform midpoint and reciprocal-factorial bounds](research_uniform_factorial_and_boundary_decay.md),
not from a bulk expansion at a singular endpoint.

On a combined side, \(Nx=-1/2+iNs\). The denominator factor is
therefore covered directly by the midpoint estimate at \(w=is\),
including \(s=0\). The numerator is
\(N(x+y)=N(b+i(s+t))-1/2\), with \(b\) in the retained compact
interval, and is covered by the same estimate. The factors involving
\(Ny\) alone stay in a fixed bulk strip. The original midpoint
Newton factors are covered by the reciprocal bound even when a
free-boundary factorial argument becomes negative.

On an \(x\)-horizontal contour the denominator \(G_N(Nx)\) has
fixed nonzero height. The
[uniform half-plane factorial continuation](research_factorial_uniform_halfplane_continuation.md)
therefore bounds it above and below on the required compact set.
For its numerator, \(w=x+y\) has real part in a compact subinterval
of \((0,3/2]\), but its height can cross zero and its real part can
cross one. Use the exact reflection
\[
                   G_N(Nw)=\frac{N}{G_N(N(1-w)-1)}.
\]
Write its denominator as a midpoint factorial with argument
\(1-w-1/(2N)\), and apply the uniform reciprocal bound. On matching
side branches \(J(1-w)=-J(w)\). The displacement \(1/(2N)\) costs
only \(O(\log N)\) in the exponent, by (9). Hence this numerator
has a uniform polynomial prefactor times \(e^{N\Re J(w)}\), even
at its zeros. This proves the needed upper estimate throughout the
horizontal-endpoint faces as well.

These arguments cover every factor in all nine terms. Polynomial
prefactors and the finite contour lengths can be absorbed into one
\(CN^A\). On the actual retained interval, for sufficiently small
complex \(u\), its midpoint Newton arguments stay on regular
branches near their values at zero. Their phases vary uniformly on
the compact contours. Thus (12) persists, with a slightly larger
bound still below \(M\), on a fixed complex disk in \(u\).

## 6. Dependence on a real boundary angle

Section 4 of the uniform-factorial note already proves, for the
exact Newton upper exponent \(\mathfrak b\),
\[
 \mathfrak b(b+it,u)-\mathfrak b(b+it,0)
 \le-\frac{\sin(2\pi b)}{4\pi\cosh^2(\pi t)}(1-\cos u),
                  \qquad -\pi\le u\le\pi.             \tag{13}
\]
It includes moving zeros and both signs of \(t\). The retained
interval has \(\epsilon/2\le b\le1/2-\epsilon/2\), and
\(|t|\le K\). Consequently every contour integrand gains the
common extra loss
\[
 c_0(1-\cos u),\qquad
             c_0=\frac{\sin(\pi\epsilon)}
                             {4\pi\cosh^2(\pi K)}>0.   \tag{14}
\]
This statement uses the uniform reciprocal-factorial estimate for
all real \(u\), rather than extending a small-disk asymptotic to the
whole period. In particular none of the nonprincipal bounds grows
when the real boundary angle is moved away from zero.

## 7. Reproduction

Run

```sh
python3 experiments/verify_mixed_two_crossing_contour_faces.py --precision 128 \
  --output repro/results/research-mixed-two-crossing-contour-faces.json
```

The compact rectangle certificates are saved by this command.
The corner proof, endpoint modulus, half-grid allowances and exact
factorial estimates are proved above and are not inferred from
numerical samples.
