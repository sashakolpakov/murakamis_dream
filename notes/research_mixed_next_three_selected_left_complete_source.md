# The complete source on the upper-left contour

Private research deduction, 8 November 2026. The estimates for the
individual incoming paths now give an exponential bound for the
entire source on the upper-left part of the shared contour. The
original filter correction is included. The proof below records the
assembly and its exact scope; it does not assert noncancellation of
the full transfer.

## 1. The source and its parameters

Keep an actual complete word in the original powers three and four
beginning \(343\), of length at least five. Use its original coupled
reference
\[
(a_*,s_*,y_*,t_*,z_*)=(t_1,s_2,t_2,s_3,t_3),
\]
its fixed heights, and its affine comparison rate
\(\Lambda_{123}(z)\). In particular put
\[
h_a=\Im a_*,\quad h_z=\Im z_*,\quad H=1/100,\qquad
y=q+iH,\quad 0\le q\le11/50,\qquad
z=u+ih_z,\quad 3/10\le u\le39/100.
\tag{1}
\]
All reference correlations are those in the component theorems
cited below. We do not replace their reference by independently
chosen parameters. The ordinary input variable satisfies
\(-2\le w\le2\).

For \(D=N-1\) and \(r=e^{-2\pi i/N}\), set
\[
\begin{split}
P_j&=(r;r)_j,\qquad p_j(V)=(rV;r)_j,\\
U_{0,N}(w,X)&=\sum_{j=0}^{D}H_N(w,r^{-j})p_j(X)/P_j,\\
C_{\beta,N}(V,W)&=\sum_{j=0}^{D}
       \frac{V^{-j}p_j(V)p_j(W)}{P_j^{2+\beta}},\\
X&=e^{-2\pi ia},\qquad Y=e^{-2\pi iy},\qquad Z=e^{-2\pi iz}.
\end{split}
\tag{2}
\]
Here \(H_N\) is the original complete coefficient, including its
internal signed sum. The polynomial \(d_N\), of degree at most
\(D\), retains its defining values \(d_N(r^b)=P_b^{-1}\).

The complete first source and the unchanged filtered source are
\[
F_N(w,Y)=N\int_{\Gamma_a}U_{0,N}(w,X)C_{1,N}(X,Y)\,da,\qquad
F_N^{\mathrm{mid}}=F_N-E_N^{\mathrm{filt}}.
\tag{3}
\]
The original contour \(\Gamma_a\) is specified in Section 2.
The correction \(E_N^{\mathrm{filt}}\) is exactly the original
deletion and interpolation correction; no new filter is applied
to any of the incoming paths.

Define the two meromorphic densities
\[
K_N^F(y)=\frac{N F_N(w,Y)d_N(Y)C_{0,N}(Y,Z)}{1-Y^N},\qquad
K_N^{\mathrm{mid}}(y)=
\frac{N F_N^{\mathrm{mid}}(w,Y)d_N(Y)C_{0,N}(Y,Z)}{1-Y^N}.
\tag{4}
\]
There is no outgoing halfweight for this next factor. The factor
\(N\) in (4) is distinct from the incoming factor \(N\) in (3).

**Theorem.** On (1), uniformly in the real ordinary input and both
level parities, there are constants \(C,B\) such that, for all
sufficiently large \(N\),
\[
\begin{split}
|F_N(w,Y)d_N(Y)Y^{-N}C_{0,N}(Y,Z)|
   &\le CN^B e^{N\{\Lambda_{123}(z)-1/10000\}},\\
|K_N^F(y)|+|K_N^{\mathrm{mid}}(y)|
   &\le CN^B e^{N\{\Lambda_{123}(z)-1/10000\}}.
\end{split}
\tag{5}
\]
The same exponential bound holds after integrating either density
over any subinterval of the upper-left segment in (1), in either
orientation. This is a bound for the complete finite source on that
segment, including \(q=0\). No new derivative assertion is made.

## 2. Every incoming path is accounted for

The original increasing contour is the following concatenation:
\[
\begin{split}
\Gamma_{\mathrm{in}}&=[0,1/10],\\
\Gamma_{\mathrm{tap}}&:
a=x-i\lambda(x-1/10),\quad
1/10\le x\le11/50,\quad \lambda=-h_a/(3/25),\\
\Gamma_{\mathrm{cen}}&=[11/50,9/20]+ih_a,\\
\Gamma_{\mathrm{hor}}&=[9/20,1/2]+ih_a,\\
\Gamma_C&=[1/2+ih_a,1/2]\ \cup\ [1/2,7/10],\\
\Gamma_{\mathrm{far}}&=[7/10,1].
\end{split}
\tag{6}
\]
Thus \(\Gamma_a\) runs from zero to one, with no omitted side
between its pieces. This is the exact incoming cycle of
[the complete lower-left assembly, Section 2](research_mixed_next_three_actual_complete_lower_left.md).
That identity is for the finite Laurent polynomials in (2) and
does not restrict the outgoing height to the lower contour.

For each path in (6), put
\[
F_N^\Gamma(w,Y)=N\int_\Gamma U_{0,N}(w,X)C_{1,N}(X,Y)\,da .
\tag{7}
\]
The following complete estimates have the same parameters (1),
the same next factor \(C_{0,N}\), and the same full weight:

| Incoming contribution | Bound for \(F_N^\Gamma d_N(Y)Y^{-N}C_{0,N}\) | Proof |
| --- | --- | --- |
| Initial segment and taper, separately | Rate at most \(\Lambda_{123}-1/10000\) | [Initial and taper theorem](research_mixed_next_three_selected_left_incoming_initial_taper.md) |
| Central horizontal segment | Rate at most \(\Lambda_{123}-1/200\) | [Central completion](research_mixed_next_three_selected_left_central_completion.md) |
| Right horizontal segment | Rate at most \(\Lambda_{123}-1/4000\) | [Right horizontal theorem](research_mixed_next_three_selected_left_incoming_right_horizontal.md) |
| The entire oriented corner \(\Gamma_C\) | Rate at most \(\Lambda_{123}-1/4000\) | [Complete corner theorem](research_mixed_next_three_selected_left_incoming_corner.md) |
| Far real segment | Rate at most \(\Lambda_{123}-1/2000\) | [Incoming end theorem](research_mixed_next_three_selected_left_incoming_ends.md) |

Each bound permits a fixed polynomial prefactor. In the corner row,
the theorem first bounds a replacement horizontal-and-vertical
path. The finite integrand is entire in \(a\), so Cauchy's theorem
identifies its integral with the original oriented union
\(\Gamma_C\). We use that equality. We do not take absolute values
on the two old corner pieces separately.

The outside factors \(d_N(Y)Y^{-N}C_{0,N}(Y,Z)\) do not depend
on \(a\). Therefore
\[
F_N d_N(Y)Y^{-N}C_{0,N}
 =\sum_{\Gamma\ \text{in }(6)}
       F_N^\Gamma d_N(Y)Y^{-N}C_{0,N}.
\tag{8}
\]
There are six fixed pieces, with both initial and taper included.
The triangle inequality and the smallest gap in the table prove
the first line of (5). All private summation indices, endpoint
terms and contour corrections were included before invoking
the component theorems.

## 3. The original filter and the paired denominator

The correction theorem
[for the selected left interval](research_mixed_next_three_selected_left_filter_correction.md)
proves
\[
|E_N^{\mathrm{filt}}d_N(Y)Y^{-N}C_{0,N}(Y,Z)|
 \le CN^B e^{N\{\Lambda_{123}(z)-1/2000\}}
\tag{9}
\]
on the entire closed interval (1). Its proof retains the
full interpolation polynomial, including its forcing term.
Combining (8) and (9) gives the same bound with gap \(1/10000\)
for \(F_N^{\mathrm{mid}}d_N(Y)Y^{-N}C_{0,N}\).

At the prescribed height \(|Y|=e^{\pi/50}>1\), exactly
\[
\frac{N F_N^{\mathrm{mid}}d_N(Y)C_{0,N}(Y,Z)}{1-Y^N}
 =-\frac{N F_N^{\mathrm{mid}}d_N(Y)Y^{-N}C_{0,N}(Y,Z)}
              {1-Y^{-N}}.
\tag{10}
\]
The denominator on the right has modulus at least
\(1-e^{-\pi N/50}\), hence at least \(1/2\) for sufficiently
large \(N\). The same identity applies to \(F_N\). The extra
factor \(N\) costs only a power of \(N\), proving the second
line of (5). Integrating over a segment of length at most
\(11/50\) proves its integral consequence.

In particular the term
\[
-\int_{[s,11/50]+i/100}K_N^{\mathrm{mid}}(y)\,dy,
\qquad 0\le s\le11/50,
\tag{11}
\]
in the original signed remainder is exponentially smaller than
the comparison rate. Its minus sign is unchanged.

The other terms of that remainder are not estimated here.
They include the paired right contribution, its vertical
boundary at the half-period, and the coherent physical sum
over the middle index range. Establishing (5) therefore removes
one complete contour obligation; it does not supply a lower
bound for the full original quantum sum.
