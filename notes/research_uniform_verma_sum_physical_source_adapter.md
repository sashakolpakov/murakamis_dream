# A uniform Verma sum has the original finite-color restrictions

This private note removes a source-choice ambiguity once a uniform
sectorial sum has actually been constructed. It does not construct that
sum. The formal restrictions are those of the original cut, pivot, and
zero framing in [C], and the analytic identification below preserves them.

## 1. Precise analytic hypothesis and conclusion

Use the natural meridian and quantum coordinate

\[
 h=\log Q,\quad q=e^{h/2},\quad
 \widehat{\mathscr W}(h,Y)=\mathcal W_K(1-e^h,Y)
                         =\sum_{j\ge0}h^j w_j(Y).
 \tag{1}
\]

The coefficients in [C] are rational and regular near \(Y=1\), with
\(w_0=\Delta_K^{-1}\). Fix a disk \(D\) about \(1\) avoiding zero
and the Alexander roots. Suppose \(S(h,Y)\) is jointly holomorphic on
\(\Sigma\times D\), where \(\Sigma\) is a punctured sector at zero
of opening strictly greater than \(\pi\). Assume the uniform Gevrey-one
remainder property: on every smaller meridian disk and every closed
subsector of smaller opening, there are constants \(C,A,r>0\) such that

\[
 \left|S(h,Y)-\sum_{j=0}^{n-1}h^j w_j(Y)\right|
                   \le C A^n n! |h|^n,
 \qquad 0<|h|<r,\quad n\ge0.
 \tag{2}
\]

For \(n=0\), the sum is empty. Constants may depend on the smaller
sets, but not on \(n,h,Y\) there.

**Source identification.** For each fixed positive integer \(L\),

\[
                         S(h,e^{Lh})=C_L(e^{h/2})
 \tag{3}
\]

for all sufficiently small \(h\) in the component of the sector under
consideration. Here \(C_L\) is exactly the original reduced, zero-framed
finite-color polynomial of [C]. No scalar normalization is adjustable.
The small radius and estimates in this assertion may depend on \(L\).

Every analytic continuation of this pullback along the lifted color
curve \((h,Y)=(h,e^{Lh})\) continues the same entire function
\(C_L(e^{h/2})\). In particular, if the candidate can be continued
along that curve to \(h=2\pi i/L\), its continued pullback has the
original complete-color value \(C_L(e^{\pi i/L})\).

The theorem does not assert that such a two-variable continuation exists,
or that its endpoint is the initial sheet of \(S(h,1)\). The lift
\(u=Lh\), and hence the full meridian path \(Y=e^u\), must be retained.

## 2. Analytic substitution preserves the required remainder

Fix a closed subsector of opening still greater than \(\pi\), and two
nested meridian disks compactly contained in \(D\). From (2), subtract
the remainders of orders \(j\) and \(j+1\), divide by \(|h|^j\), and
let \(h\) tend to zero along an interior ray. This gives

\[
                  \sup |w_j(Y)|\le C A^j j!
 \tag{4}
\]

on the smaller disk, after increasing fixed constants if necessary.
Choose \(r_L>0\) so that \(e^{Lh}\) remains in this disk whenever
\(|h|\le r_L\). For example a sufficiently small constant divided by
\(L\) suffices. Each \(f_j(h)=w_j(e^{Lh})\) is holomorphic on that
disk and has the bound (4).

For \(|h|\le r_L/2\), Cauchy's coefficient estimate gives

\[
 \left|f_j(h)-\sum_{a=0}^{n-j-1}[h^a]f_j\,h^a\right|
       \le 2 C A^j j!(|h|/r_L)^{n-j},\qquad j<n.
 \tag{5}
\]

Multiply (5) by \(|h|^j\) and sum. Since \(j!\le n!\) and
\(n\le2^n\), the result is at most
\(K_L A_L^n n!|h|^n\). Combining it with (2) shows that the pullback
\(S(h,e^{Lh})\) has a uniform Gevrey-one asymptotic expansion whose
formal series is the formal substitution in (1).

[C, (10)] gives exactly

\[
 \widehat{\mathscr W}(h,e^{Lh})=C_L(e^{h/2})
                         \quad\text{as formal series}.
 \tag{6}
\]

The right side is an entire function of \(h\): it is a finite Laurent
polynomial in \(q=e^{h/2}\). Its convergent Taylor expansion also has
Gevrey-one remainder bounds on a smaller disk. Therefore

\[
 F_L(h):=S(h,e^{Lh})-C_L(e^{h/2})
 \quad\text{satisfies}\quad
 |F_L(h)|\le K_L B_L^n n!|h|^n
 \quad\text{for every }n.
 \tag{7}
\]

Only a fixed-color assertion has been used here. There is no uniform
large-\(L\) estimate implicit in (5)--(7).

## 3. An elementary flat-uniqueness proof

We prove the uniqueness fact needed for (7). Suppose \(F\) is
holomorphic on a sector of opening greater than \(\pi\), and on a
closed subsector of opening still greater than \(\pi\) obeys
\(|F(h)|\le C B^n n!|h|^n\) for every \(n\).
Choose \(n=\lfloor(2B|h|)^{-1}\rfloor\) and use \(n!\le n^n\).
For sufficiently small \(h\), this gives constants \(C_0,a>0\) with

\[
                         |F(h)|\le C_0 e^{-a/|h|}.
 \tag{8}
\]

Rotate the sector and set \(g(z)=F(e^{i\theta_0}/z)\). Because its
opening exceeds \(\pi\), a right half-plane \(\Re z>x_0\) lies in
the transformed closed subsector, with

\[
                       |g(z)|\le C_0e^{-a|z|}.
 \tag{9}
\]

For real \(x>x_0\), define the vertical integral

\[
 H_x(t)=\int_{x-i\infty}^{x+i\infty}g(z)e^{tz}\,dz.
 \tag{10}
\]

It is holomorphic on the strip \(|\Im t|<a\). Integrating over a
rectangle between two vertical lines, the horizontal contributions
tend to zero by (9), locally uniformly in that strip. Thus \(H_x(t)\)
is independent of \(x\); denote it by \(H(t)\).

For real \(t<a/\sqrt2\), the inequality
\(|x+iy|\ge(x+|y|)/\sqrt2\), with \(x>0\), gives
\(|H_x(t)|\le C_1e^{(t-a/\sqrt2)x}\). Sending \(x\) to infinity
proves \(H(t)=0\) on a real open interval. The identity theorem makes
\(H\) zero throughout its strip, in particular for every real
\(t\ge0\).

Fix \(w\) with \(\Re w>x>x_0\). Cauchy's formula on the right
half-disk, whose semicircle contribution tends to zero by (9), is

\[
 g(w)={1\over2\pi i}\int_{x-i\infty}^{x+i\infty}
                            {g(z)\over w-z}\,dz
     ={1\over2\pi i}\int_0^\infty e^{-tw}H(t)\,dt=0.
 \tag{11}
\]

The second equality uses
\((w-z)^{-1}=\int_0^\infty e^{-t(w-z)}dt\); absolute integrability
follows from \(\Re w>x\) and (9). Hence \(g=0\), and the identity
theorem gives \(F=0\) on its original sector. This proves flat
uniqueness without a separate summability theorem.

Applying it to (7) proves (3). Ordinary uniqueness of analytic
continuation then proves the color-curve assertion in Section 1.
The entire continuation available for the scalar \(C_L\) is not a
construction of a two-variable continuation of \(S\).

## 4. What the actual recurrence supplies at the anchor

The analytic hypothesis (2) has not been constructed by this argument.
In particular, actual initial colors are not already a uniform
sectorial remainder estimate. There is a precise degeneration in the
displayed original normal-state equation.

Let an actual normal-state operator with coefficients holomorphic near
\((h,Y)=(0,1)\) annihilate
\(v=(Y-1)\widehat{\mathscr W}\). Write its classical symbol as
\(P(Y,L)\), its order-\(h\) coefficient sum as \(P_1(Y,1)\), and
put \(p(Y)=P_L(Y,1)\). [C] gives \(P(Y,1)\equiv0\).
Direct expansion of the original left-ordered shifts gives

\[
 Yp(Y)v_0'(Y)+P_1(Y,1)v_0(Y)=0,
 \qquad v_0=(Y-1)/\Delta_K(Y).
 \tag{12}
\]

Consequently

\[
 P_1(Y,1)=Yp(Y)
       \left({\Delta_K'(Y)\over\Delta_K(Y)}-{1\over Y-1}\right).
 \tag{13}
\]

Since \(\Delta_K(1)=1\), holomorphy forces \(p(1)=0\), and
\(P_1(1,1)=-p'(1)\). Composing the full operator on the right with
\(Y-1\) gives an operator for the reduced source. Its first-order
\(h\) term is exactly

\[
       Y(Y-1)p(Y)
          \left(\partial_Y+{\Delta_K'(Y)\over\Delta_K(Y)}\right).
 \tag{14}
\]

Thus this displayed transport vanishes at least quadratically at
\(Y=1\). Dividing that factor from its first-order term does not
justify dividing it from the entire analytic quantum operator:
higher terms may have no such factor. No uniformly bounded transport
inverse at the anchor follows from (12)--(14). These identities do not
exclude a different, independently justified source-compatible
desingularization.

The anchor nevertheless has an exact all-order boundary row. In
fixed-\(x\) coordinates, [C, (10)] at \(L=1\) says
\(\widehat V(1-e^h,1)=1\) formally; in natural coordinates it is
\(\widehat{\mathscr W}(h,e^h)=1\). Under (2), (3) makes that identity
analytic. It is not the identity \(S(h,1)=1\).

The remaining analytic task is to construct a holomorphic function on
an actual product of a sector wider than \(\pi\) and a meridian
neighborhood with (2), or to prove a summation theorem that supplies
those properties for this source. Coefficient Gevrey bounds, finite
Borel-path continuation, and finite-color initial values do not by
themselves supply its remainder bound. Once it is supplied, (3) shows
that there is no further local finite-color source choice to make.
Global continuation along the lifted color curves and large-level
growth estimates remain separate tasks.

## 5. Complete proof source and scope

The sole proof direct is:

| Label | Complete source | SHA256 |
|---|---|---|
| C | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |

C supplies the original formal color restrictions and normal-state
compatibility. The substitution estimates, flat-uniqueness contour
argument, analytic identification, and anchor degeneration are proved
above. The uniqueness principle is established mathematics; no novelty
is claimed for it and no external proof is imported.

This is an exact source adapter under its explicit analytic hypothesis,
not a construction of a generic-quantum period or a volume lower bound.
Only written mathematics and source-text reads were used; frozen notes
and public manuscripts are unchanged.
