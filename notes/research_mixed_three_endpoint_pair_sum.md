# The type-three endpoint pair lies beyond the half-angle

Research lemma, 5 November 2026. The original type-three unit equation,
the complete-end cotangent barrier, and the unit cotangent cone imply
the endpoint sum needed by the open-word injectivity argument. The
proof is algebraic and uses no new root enclosure.

## 1. The actual endpoint variables

At a type-three unit vertex adjacent to a complete outside vertex,
let \(s\) be its private inverse leg and \(t\) its other inverse leg.
Use the original wire cotangent and the two leg cotangents
\[
 q=P-ih,\qquad p=\cot\pi s,\qquad v=\cot\pi t.
 \tag{1}
\]
The original inverse-leg branches give \(0<\Re s,\Re t<1/2\)
and \(\Re p,\Re v>0\). The
[complete-end barrier](research_mixed_endpoint_cotangent_barrier.md)
gives \(0<h<1\): the selected unit vertex is active, so the
wire height \(h\) is positive. Put
\[
             k=1-h\in(0,1),\qquad r=q+i=P+ik.
 \tag{2}
\]
At the complete outside end its inverse cosine square is one.
Thus the selected inverse cosine square is \(\alpha=q^2\).
The incidence identity and the own type-three unit identity give
\[
     p=q-\frac1r,\qquad
     \alpha=-(p+i)(v+i),\qquad
     v=-\frac{q^2}{p+i}-i.
 \tag{3}
\]
The only additional cone inequality used below is
\(\Im v<1\), supplied by
[the unit cotangent bounds](research_mixed_unit_cotangent_bounds.md).
In particular this proof does not assume an endpoint sum condition.

## 2. Eliminating the two inverse legs

Since \(P>0\), \(r\ne0\). Also
\[
        p+i=r-\frac1r=\frac{r^2-1}{r}\ne0,
 \tag{4}
\]
because \(\Re p>0\). The cotangent addition identity,
followed by (3), gives exactly
\[
       \cot\pi(s+t)=\frac{pv-1}{p+v}=r^3-r-i.
 \tag{5}
\]
Here \(p+v\ne0\), again by positivity of its real part.
Writing \(T=P^2\), its real part is
\[
              \Re\cot\pi(s+t)=P(T-3k^2-1).
 \tag{6}
\]
It remains to prove \(T<1+3k^2\).

The real part of the first identity in (3) gives
\[
       \Re p=P\left(1-\frac1{P^2+k^2}\right)>0,
             \qquad P^2+k^2>1.
 \tag{7}
\]
The real part of the last identity gives
\[
 \Re v
  =\frac{P\{4k(1-k)-(P^2+k^2-1)^2\}}
                 {|r^2-1|^2}>0.
 \tag{8}
\]
Therefore
\[
          1<P^2+k^2<1+2\sqrt{k(1-k)}\le2.
 \tag{9}
\]

If \(k\ge1/2\), (9) immediately yields
\[
             T<2-k^2\le1+3k^2.
 \tag{10}
\]
Suppose instead \(0<k<1/2\). Directly from (3),
\[
\begin{split}
 (\Im v-1)|r^2-1|^2&=f_k(T),\\
 f_k(T)&=-kT^2+(2+2k-2k^3)T\\
       &\hspace{8mm}-k^5-2k^3-2k^2-k-2 .
\end{split}
\tag{11}
\]
The exact value at the proposed threshold is
\[
 f_k(1+3k^2)
        =-4k^2(2k-1)(2k^2+k+1)>0.
 \tag{12}
\]
If \(T\ge1+3k^2\), then \(T<2\) by (9), and on the
whole interval between these values
\[
 f_k'(T)=2(1+k-k^3-kT)
             >2(1-k-k^3)>0.
 \tag{13}
\]
Thus \(f_k(T)>0\), contradicting \(\Im v<1\) in (11).
This proves \(T<1+3k^2\) also in the second case.

**Theorem 1.** Every type-three endpoint vertex of the original
positive unit path satisfies
\[
                         \Re(s+t)>1/2.
 \tag{14}
\]
Indeed (6) is strictly negative. Since
\(0<\Re(s+t)<1\), the formula
\[
 \Re\cot\pi z
   =\frac{\sin(2\pi\Re z)}
          {\cosh(2\pi\Im z)-\cos(2\pi\Re z)}
 \tag{15}
\]
has a positive denominator and is negative exactly when
\(\Re z>1/2\). This proves (14).

Either endpoint orientation is included by exchanging \(s,t\).
For a one-vertex type-three word, either of its two complete
outside incidences gives the same argument. For a type-four
endpoint no corresponding sum inequality is required by
[the cotangent-cone Hessian lemma](research_mixed_cotangent_cone_injectivity.md#2-what-this-gives-for-the-full-open-word).
The theorem is a geometric coordinate statement, not a finite-source
or full open-chain asymptotic estimate.

