# The complete three-negative-crossing connection formula

Research deduction, 7 November 2026. The exact forced difference
equation determines the signed endpoint current after three negative
crossings. Its apparent square-root loss in the absolute contour
bound is removed by two nested Cauchy estimates. The resulting
connection formula retains the canonical pole product and every
finite periodic zero.

On fixed negative incoming heights, including the actual type-four
family, the endpoint current leads the whole crossed function.
The canonical pole product is exponentially smaller there.
At physical incoming nodes the current instead vanishes exactly.
No numerical evaluation or asymptotic replacement of a finite
crossing matrix is used.

## 1. Exact normalization of the signed current

Keep all notation and the exact identity
\[
       G_{-3}(a,y)=\mathcal P_{-3,N}(a,y)
                              +\mathcal J_{-3,N}(a,y)
\tag{1}
\]
from [the complete pole/current theorem](research_mixed_fourier_negative_three_pole_current.md).
Throughout the first two sections the parameters range over compact
subsets of
\[
 \mathcal D=\{\,0<\Re a<1/2,\quad 0<\Re y<1/2,\quad \Im y>0\,\}.
\tag{2}
\]
Set \(X=e^{-2\pi ia}\), \(Y=e^{2\pi iy}\),
\(r=e^{-2\pi i/N}\), \(D=N-1\), and retain the original
unit crossing scalar \(\kappa\).

Let \(Q_N(v;a,y)\) be exactly the integrand in equations
(18)--(19) of the pole/current note:
\[
 Q_N(v)=
 \frac{e^{2\pi Nv}}{(1+e^{2\pi Nv})^2}
 \frac{R_N(\alpha_N+iv;a)}
      {1-Y^{-1}r e^{-2\pi i(\alpha_N+iv)}},
 \qquad \alpha_N=-\frac1{2N}.
\]
Define the holomorphic function
\[
                         V_N(a,y)=-iN^2\int_{\mathbb R}Q_N(v;a,y)\,dv.
\tag{3}
\]
This integral definition is used also where \(X^N=1\).
The proved compact-uniform tail bounds justify holomorphy in
both parameters and give
\[
                         |V_N(a,y)|\le C\sqrt N .
\tag{4}
\]
In particular no finite periodic factor has been divided out.
The exact current is
\[
 \boxed{\quad
 \mathcal J_{-3,N}(a,y)=
 \kappa^{-3}N^{-3}e^{\pi iDy}
       (1-Y^{-N})(X^{-N}-1)V_N(a,y).
 \quad}
\tag{5}
\]

The canonical pole term obeys an exact homogeneous equation.
Its definition is
\[
 \mathcal P_{-3,N}=\frac{\kappa^{-3}e^{\pi iDy}}N
    e^{2\pi iNa s_0}\Pi_N(s_0+a)E_N(a)E_N(s_0),
 \qquad s_0=1-y-\frac1N .
\]
The one-step factorial recurrence gives, as an undivided identity,
\[
 (1-rX)\mathcal P_{-3,N}(a+1/N,y)
                =(r/Y-rX)\mathcal P_{-3,N}(a,y).
\tag{6}
\]
Indeed \(e^{2\pi is_0}=r/Y\) and
\(e^{-2\pi i(s_0+a+1/N)}=XY\).
This proves (6) even when its numerator vanishes.

The exact full-source equation (12) of
[the three-negative-crossing reduction](research_mixed_fourier_negative_three_full_source.md)
is
\[
 \begin{split}
 &(1-rX)G_{-3}(a+1/N,y)-(r/Y-rX)G_{-3}(a,y)\\
 &\hspace{12mm}
  =\frac{\kappa^{-3}e^{\pi iDy}(1-Y^{-N})}{N^3}
        \sum_{k=0}^{D}(r^{-1}/X)^k .
 \end{split}
\tag{7}
\]
The finite geometric identity is
\[
 \sum_{k=0}^{D}(r^{-1}/X)^k
             =(X^{-N}-1)\frac{rX}{1-rX}.
\tag{8}
\]
The factor \(X^{-N}-1\) is unchanged by \(a\mapsto a+1/N\).
Subtract (6) from (7), insert (5), and first work off its
isolated zeros. Holomorphy then extends the result across them:
\[
 \boxed{\quad
 (1-rX)V_N(a+1/N,y)-(r/Y-rX)V_N(a,y)
                              =\frac{rX}{1-rX}.
 \quad}
\tag{9}
\]
On every fixed compact subset of (2), all displayed denominators
are nonzero for sufficiently large \(N\). This is a consequence
of \(X\ne1\) there and \(|Y|<1\), not removal of a physical zero.

## 2. The uniform signed-current asymptotic

**Theorem 1.** On every compact subset of \(\mathcal D\),
\[
 \boxed{\quad
 V_N(a,y)=
       \frac{XY}{(1-X)(Y-1)}+O(N^{-1}).
 \quad}
\tag{10}
\]
The error is holomorphic and has order \(O(N^{-1})\) with
every fixed parameter derivative on smaller compact subsets.
In particular its leading coefficient is nonzero.

*Proof.* Choose three nested relatively compact parameter
neighborhoods inside \(\mathcal D\), with positive distances
between their boundaries. Equation (4) holds on the largest.
Cauchy's estimate on the next neighborhood gives
\[
 V_N(a+1/N,y)-V_N(a,y)=O(N^{-1/2}),
\tag{11}
\]
uniformly where the small segment stays in that neighborhood.
Rewrite (9) as
\[
 (1-r/Y)V_N(a,y)
   =\frac{rX}{1-rX}
       -(1-rX)\{V_N(a+1/N,y)-V_N(a,y)\}.
\tag{12}
\]
Here \(|1-r/Y|\) has a uniform positive lower bound, because
\(|Y|\le\rho<1\). Equations (11)--(12) improve (4) to the
uniform bound \(V_N=O(1)\) on the middle neighborhood.

A second Cauchy estimate on a smaller neighborhood now improves
(11) to \(O(N^{-1})\). Hence
\[
 V_N(a,y)=\frac{rX}{(1-rX)(1-r/Y)}+O(N^{-1}).
\tag{13}
\]
Since \(r=1+O(N^{-1})\), its leading expression is exactly
the fraction in (10). A final nested Cauchy estimate proves
the fixed derivative assertion for the holomorphic error.
Compact sets are covered by finitely many such neighborhoods.
No assertion about the pointwise exponent of the earlier
absolute current estimate is used. \(\square\)

Combining (1), (5), and (10) gives the full connection formula
\[
 \boxed{\begin{split}
 G_{-3}(a,y)
   ={}&\mathcal P_{-3,N}(a,y)\\
     &+\kappa^{-3}N^{-3}e^{\pi i(N-1)y}
       (1-Y^{-N})(X^{-N}-1)
       \left\{\frac{XY}{(1-X)(Y-1)}+O(N^{-1})\right\}.
 \end{split}}
\tag{14}
\]
The bracket, rather than the whole rapidly varying expression,
has the stated fixed-jet error. Both finite periodic factors
are exact. Thus (14) remains valid at \(X^N=1\), where its
entire second line is exactly zero and the pole term equals
the complete source.

## 3. Physical evaluations do not identify Hermite normals

The integral-defined \(V_N\) also makes the physical incoming
derivatives explicit. At \(a=b/N\), \(0<b<N/2\), the value
\(\mathcal J_{-3,N}\) is zero, but
\[
 \boxed{\quad
 \partial_a\mathcal J_{-3,N}(b/N,y)
   =2\pi i\,\kappa^{-3}N^{-2}e^{\pi iDy}
             (1-Y^{-N})V_N(b/N,y).
 \quad}
\tag{14a}
\]
More generally, for every fixed integer \(k\ge1\),
\[
 \left.\partial_a^k\mathcal J_{-3,N}\right|_{a=b/N}
 =\kappa^{-3}N^{-3}e^{\pi iDy}(1-Y^{-N})
      \sum_{r_0=1}^k {k\choose r_0}(2\pi iN)^{r_0}
           \partial_a^{k-r_0}V_N(b/N,y).
\tag{14b}
\]
The summation index \(r_0\) is unrelated to the root of unity \(r\).
These are exact identities, obtained by differentiating the
periodic factor before evaluating it at its zero.
Uniformly for \(b/N\) in a compact subset of \((0,1/2)\),
the fixed-jet version of (10) gives
\[
 \left.\partial_a^k\mathcal J_{-3,N}\right|_{a=b/N}
  =(2\pi i)^k\kappa^{-3}N^{k-3}e^{\pi iDy}(1-Y^{-N})
       \left\{\frac{XY}{(1-X)(Y-1)}+O(N^{-1})\right\}.
\tag{14c}
\]
Its leading coefficient is nonzero. Thus physical value observations
may replace the whole source by the pole product exactly, whereas
parameter Hermite observations must retain (14b). Identification
of a particular closing functional with those parameter derivatives
is a separate question; no such identification is presumed here.

## 4. Which term leads on actual incoming heights

For the original outgoing parameter \(y=x_0\), the preceding
pole/current proof establishes on the whole incoming plateau
\(x=\Re a\in[11/50,9/20]\), at every admitted original height,
\[
 \Re\Phi_p(a,x_0)
       <e_{\rm end}(a,x_0)-\frac1{12},\qquad
 e_{\rm end}=2\pi(-\Im a)_++\pi\Im x_0.
\tag{15}
\]
Its canonical pole has the nonzero \(N^{-3/2}\) packet
displayed there. The strict inequality persists on a small
complex neighborhood of each such parameter.

**Corollary 2.** Suppose first that \(\Im a_*<0\).
There is a parameter neighborhood of \((a_*,x_0)\) on which
\[
 \boxed{\quad
 \mathcal M_{-3}Z_N(a,y)
   =\kappa^{-3}N^{-3}
        \frac{Xe^{\pi iy}}{(1-X)(1-Y)}
        e^{N(2\pi ia-\pi iy)}(1+O(N^{-1})).
 \quad}
\tag{16}
\]
This is a nonzero packet for the entire original crossed
Fourier function. Every fixed derivative of the normalized
holomorphic remainder has order \(O(N^{-1})\) on a smaller
neighborhood. It applies to every actual type-four incoming
reference, and to each negative-height type-three reference.
It retains both level parities through the original \(\kappa\).

*Proof.* On a smaller neighborhood, \(|X|,|Y|<1\) uniformly.
Thus \(1-Y^{-N}=-Y^{-N}(1+O(e^{-cN}))\) and
\(X^{-N}-1=X^{-N}(1+O(e^{-cN}))\).
Substituting into (14) gives exactly (16)'s phase, scalar,
and amplitude. By (15), the pole/current ratio is bounded by
a polynomial times \(e^{-N/12}\) at the center, and by
\(e^{-c'N}\) on a smaller neighborhood.
It is therefore included in the holomorphic relative error.
The nonzero amplitude and nested Cauchy estimates prove the
remaining assertions. \(\square\)

If instead \(\Im a_*>0\), the same argument on a neighborhood
with \(|X|>1\) gives
\[
 \boxed{\quad
 \mathcal M_{-3}Z_N(a,y)
   =-\kappa^{-3}N^{-3}
        \frac{Xe^{\pi iy}}{(1-X)(1-Y)}
          e^{-N\pi iy}(1+O(N^{-1})).
 \quad}
\tag{17}
\]
The different sign and incoming phase follow from
\(X^{-N}-1=-1+O(e^{-cN})\). There is no division by an incoming
Fourier weight in either packet.

At real incoming height, (14) remains the uniform statement.
It retains the oscillatory factor \(X^{-N}-1\) and its exact
zeros. No uniform dominance or noncancellation is claimed in
exponentially small neighborhoods of those zeros. In particular
the nodewise equality with the pole product did not imply that
the pole led at complex incoming parameters: (16) proves the
opposite on all actual type-four references.

The phases in (16)--(17) are the original finite-source endpoint
phases. They are not identified with a knot action or a geometric
volume. The earlier original-action upper gap is compatible with
these nonzero packets: this short signed word changes which
part of the exact source provides its leading term.
