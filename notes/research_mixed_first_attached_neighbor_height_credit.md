# The negative neighbor height improves both original incidences

Research deduction, 7 November 2026. On the actual early
first-minimum taper, replacing the negative own-four neighbor
height by zero gives a lower bound for its entire two-incidence
force. This holds throughout the taper, for the full following
regular-index height range. On the lower part of the neighbor's
real interval it gives an explicit positive quadratic credit.
The remaining regular lower bound also has its first ordinary
real index at one of two endpoints.

This is a global derivative reduction with a favorable credit,
not yet payment of the complete coupled derivative. The actual
reference, original allocations and boundary charges are unchanged.

## 1. The original force, including both incidences

Use the actual source restrictions of
[the two-incidence reduction](research_mixed_first_attached_two_incidence_reduction.md)
and the
[coupled seam theorem](research_mixed_first_attached_coupled_seam_transport.md).
In particular,
\[
 \begin{gathered}
 a=x-i\lambda_a d,\quad b=z-i\lambda_b d,\quad d=x-.1,
 \qquad .1\le x\le.22,\quad x\le z\le.5,\\
 0\le\lambda_b\le17/20,\qquad
 -7/40\le\lambda_a\le3/5\quad(\alpha=0),\\
 1/6<\lambda_a<13/20\quad(\alpha=1).
 \end{gathered}                                                \tag{1}
\]
The own-four first coefficient remains the actual unattenuated
attached coefficient with \(m\ge3\). The same \(\lambda_b\)
occurs in the neighbor's height and its derivative; its actual
upper cutoff is retained. The first coordinate supplies both
active minima, and a following ordinary regular profile must
independently be valid on the target domain.

The original index-height reduction gives
\[
 \mathcal H(e,v,\eta,t)\ge
 \mathcal H(e,v,0,t)+\frac{47\pi}{2009}(-\eta),
                  \qquad -.108\le\eta\le0.                  \tag{2}
\]
We therefore take the first ordinary index \(s=v\) real.
The new
[upper index barrier](research_mixed_first_attached_four_upper_index_barrier.md)
and the old lower barrier permit
\[
 .22\le v\le.4,\qquad
 t=w+i\zeta,\quad .22\le w\le.49,\quad -.108\le\zeta\le.068 .
                                                               \tag{3}
\]
The following index is not required to have nonpositive height.

For a temporary neighbor height \(h\in[-.108,0]\), put
\[
 \begin{split}
 B(v,t;z,h)&=\Im\{g'(v+z+ih)+g'(t+z+ih)
                                -3g'(z+ih)+2\pi it\},\\
 B_{\rm end}(t;z,h)&=
       \Im\{g'(t+z+ih)-2g'(z+ih)+2\pi it\}.
 \end{split}                                                  \tag{4}
\]
The second line is the exact neighboring force when the first
ordinary factor takes its true last row. It includes the following
factor and the original two halves at \(b\). The extra
\(2\pi(h_b)_+\) in that row has zero right derivative along
the actual move into negative height.

## 2. A strict monotonicity and quantitative credit

**Lemma 1.** Both functions in (4) strictly decrease as \(h\)
increases. For \(z\le.28\) they satisfy the explicit bounds
\[
 \begin{array}{c|cc}
  & .1\le z\le.2 & .2\le z\le.28\\ \hline
 \partial_h B & <-142\pi/285 & <-104\pi/87\\
 \partial_h B_{\rm end} & <-158\pi/285 & <-79\pi/87 .
 \end{array}                                                  \tag{5}
\]

*Proof.* Since \(g''=\pi\cot\pi z-\pi i\), exactly
\[
 \begin{split}
 \partial_h B/\pi
 &=\Re\cot\pi(v+z+ih)+
       \Re\cot\pi(w+z+i(h+\zeta))-3\Re\cot\pi(z+ih),\\
 \partial_h B_{\rm end}/\pi
 &=\Re\cot\pi(w+z+i(h+\zeta))-2\Re\cot\pi(z+ih).
 \end{split}                                                  \tag{6}
\]
These identities keep both incidences and all original chirps.
The following height \(\zeta\) is fixed in this differentiation.

For every real \(y\in(0,1)\) and finite \(k\),
\[
 \Re\cot\pi(y+ik)=
       \frac{\sin(2\pi y)}{\cosh(2\pi k)-\cos(2\pi y)} .
                                                               \tag{7}
\]
On \(y<1/2\) this is at most \(\cot(\pi y)\);
on \(y\ge1/2\) it is nonpositive. Also
\(\cosh(2\pi h)<5/4\) throughout the present height range:
\(.216\pi<\log2\), and
\(\cosh(\log2)=5/4\).

For \(.1\le z\le.2\), the elementary pentagon bounds give
\(\sin(2\pi z)>29/50\), \(\cos(2\pi z)>3/10\).
Consequently
\[
 \Re\cot\pi(z+ih)>\frac{58}{95}.
 \tag{8}
\]
Every shifted real argument in (6) lies in \([.32,.99]\).
Its real cotangent is less than \(2/3\), uniformly in its
height, by the cotangent bound already used in (2).
Thus the two lines in (6) are respectively less than
\(4/3-174/95=-142/285\) and
\(2/3-116/95=-158/285\).

For \(.2\le z\le.28\), use instead
\[
 \sin(2\pi z)>9/10,\qquad \cos(2\pi z)>-1/5,\qquad
 \Re\cot\pi(z+ih)>\frac{18}{29}.                            \tag{9}
\]
The sine bound follows at both ends of
\([.4\pi,.56\pi]\) from the pentagon formula and
\(\cos(.06\pi)>9/10\); the minimum is at an endpoint.
The cosine bound follows from
\(\sin(.06\pi)<1/5\).
All shifted real arguments now lie in \([.42,.99]\), so
their real cotangents are less than
\(\cot(2\pi/5)<1/3\).
The two bounds in (6) become
\(2/3-54/29=-104/87\) and
\(1/3-36/29=-79/87\).

Finally, for \(.28\le z\le.5\), every shifted real
argument belongs to \([.5,.99]\), so its real cotangent
is nonpositive. The unshifted real cotangent is positive
until \(z=.5\). At \(z=.5\) both shifted arguments
are strictly above \(1/2\), hence their real cotangents
are negative. Both derivatives in (6) are therefore
strictly negative throughout this last interval too.
This proves the lemma. \(\square\)

Define \(\mu(z)\) by the first row of the positive constants
in (5), and set \(\mu(z)=0\) for \(z>.28\). At \(z=.2\)
either valid value may be used. Define \(\mu_{\rm end}\)
similarly from the second row.
Integrating (5)--(6) at the actual height gives
\[
 \begin{split}
 \lambda_b B(v,t;z,-\lambda_b d)
    &\ge\lambda_b B(v,t;z,0)+\mu(z)\lambda_b^2d,\\
 \lambda_b B_{\rm end}(t;z,-\lambda_b d)
    &\ge\lambda_b B_{\rm end}(t;z,0)
                                      +\mu_{\rm end}(z)\lambda_b^2d .
 \end{split}                                                  \tag{10}
\]
The inequalities also hold at \(d=0\) or \(\lambda_b=0\).
No independent height-radius box was introduced.

In particular the lower neighboring-force bound proved at
the seam in the coupled theorem extends to every \(x\)
in (1), with the same full following-height range:
\[
 \lambda_b B(v,t;z,-\lambda_b d)
 >-\frac{17\pi}{20}(v+9/25)+\frac{119}{400}.
                                                               \tag{11}
\]
The analogous true-row bound is
\(-153\pi/500+119/400\).
These bounds are conservative; (10) retains additional
positive information discarded by (11).

## 3. The remaining regular lower expression has two index endpoints

Let
\[
 H_\alpha(e,v)=
 \Re\!\left[(1-i\lambda_a)
 \{g'(e+a)+g'(v+a)-(2+\alpha)g'(a)+2\pi iv\}\right].
 \tag{12}
\]
At height zero for \(b\), the original arguments give exactly
\[
 B(v,t;z,0)=
 \pi(-1-v+2z+2w)+
             \arg(1-e^{2\pi\zeta}e^{-2\pi i(w+z)}).
                                                               \tag{13}
\]
The lift in (13) is the original continuous logarithmic one.
Thus the \(v\)-dependent part of the conservative lower
expression from (10) is
\[
                         H_\alpha(e,v)-\pi\lambda_b v.
                                                               \tag{14}
\]

**Lemma 2.** The minimum of (14) on \(v\in[.22,.4]\)
is attained at one of its endpoints.

*Proof.* Write \(r=e^{-2\pi\lambda_a d}\) and
\(\theta=2\pi(x+v)\in[.64\pi,1.24\pi]\).
The sign of the \(v\) derivative of (14) is the sign of
\[
 N(\theta)=2\lambda_a(1-r\cos\theta)+2r\sin\theta
                   -\lambda_b(1+r^2-2r\cos\theta).           \tag{15}
\]
Its derivative in \(\theta\) is
\[
 N'(\theta)=2r\{\cos\theta+(\lambda_a-\lambda_b)\sin\theta\}.
                                                               \tag{16}
\]
For \(\theta\le\pi\), if \(\lambda_a\le\lambda_b\),
then \(N'<0\). If \(\lambda_a>\lambda_b\), necessarily
\(\lambda_a>0\), \(r\le1\), and
\[
 N=\lambda_a(1-r^2)+2r\sin\theta+
          (\lambda_a-\lambda_b)(1+r^2-2r\cos\theta)>0.
 \tag{17}
\]
So this latter case has no zero before \(\pi\).

For \(\pi\le\theta\le1.24\pi\), (16) is negative
when \(\lambda_a\ge\lambda_b\). In the other case use
\(\lambda_b-\lambda_a\le41/40\) and
\[
                         \cot(6\pi/25)>41/40 .
 \tag{18}
\]
For an explicit elementary witness to (18), put \(u=19/25\).
Since \(6\pi/25<u\), the cosine lower and sine upper Taylor
bounds give
\[
 40(1-u^2/2)-41(u-u^3/6+u^5/120)
          =\frac{235592441}{1171875000}>\frac15>0.
 \tag{19}
\]
Thus \(\cos\theta+(\lambda_a-\lambda_b)\sin\theta<0\)
also in this case.
Every zero of \(N\), if one occurs, is consequently a
strict downward crossing. It cannot give an interior minimum
of (14), proving the lemma. \(\square\)

The private \(e\)-endpoint reduction is unaffected by (13):
use \(e=.27,.49\) for own three and \(e=.27,.4\)
for own four. The positive credit in (10) is independent
of \(e,v\), so it is retained under these two reductions.
In particular the regular lower comparison now involves the
four \(e,v\) endpoint choices while preserving the actual
\(\lambda_a,r\), \(z,\lambda_b\), following index and both
incidences. Their complete positivity has not been inferred.

The true last row uses the second line of (10) instead.
Other physical-tail profiles require their own derivatives.
Nor does a valid following regular formula prove its full
finite-source envelope on a new target domain.
The original compensated boundary expression, middle terms
and relative pinning fee are unchanged by this local
calculation; their final calibrated payment remains open.
